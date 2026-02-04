from fastapi import FastAPI
from openai import OpenAI
import psycopg2
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

LLM_MODEL = "deepseek/deepseek-r1-0528:free"

LLM_API_KEY = os.getenv("LLM_API")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=LLM_API_KEY,
)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.get("/")
def read_root():
    return {"message": "Hello World"}


def build_prompt(question: str, phones: list[dict]) -> str:
    data_lines = []
    for p in phones:
        line = (
            f"- {p['model']}: "
            f"release_date={p.get('release_date','N/A')}, "
            f"display_size={p.get('display_size','N/A')}, "
            f"display_width={p.get('display_width','N/A')}, "
            f"display_height={p.get('display_height','N/A')}, "
            f"battery={p.get('battery','N/A')}, "
            f"camera={p.get('camera','N/A')}, "
            f"ram={p.get('ram','N/A')}, "
            f"storage={p.get('storage','N/A')}, "
            f"price={p.get('price','N/A')}"
        )
        data_lines.append(line)

    prompt = (
        f"You are a helpful assistant specialized in Samsung phones.\n\n"
        f"User question: {question}\n\n"
        f"Data:\n" + "\n".join(data_lines) + "\n\n"
        "Instructions: Based on the question and the data above, produce a concise, factual, "
        "and actionable answer. If the question asks for a comparison, highlight differences "
        "in camera, battery, display and price and give a recommendation. If the question asks "
        "for the best phone under a price, state the metric and reason. Keep the answer short "
        "(2-6 sentences) and avoid hallucinations; if data is missing say that the information "
        "is not available. Also remember the value for camera are in MegaPixel and value for ram and storage are in Gigabyte."
    )
    return prompt


def ask_LLM(question: str, phones: list[dict]) -> str:
    if not LLM_API_KEY:
        raise RuntimeError("OpenAI API key not found in environment.")

    prompt = build_prompt(question, phones)

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for phone comparisons."},
                {"role": "user", "content": prompt}
            ],
        )

        content = response.choices[0].message.content
        return content.strip()

    except Exception as e:
        return f"OpenAI API error: {str(e)}"


def get_details_message(model: dict)->str:
    message = f"Details for model '{model["model"]}' are given below:\n-release date: {model["release_date"]}\n"
    message += f"-display size: {model["display_size"]}inch\n"
    message += f"-display resolution: {model["display_width"]} x {model["display_height"]}\n"
    message += f"-battery: {model["battery"]}mph\n"
    message += f"-camera: {model["camera"]}MP\n"
    message += f"-memory: {model["ram"]}GB\n"
    message += f"-storage: {model["storage"]}GB\n"
    message += f"-price: ${model["price"]}\n"
    
    return message

class AskQuestion(BaseModel):
    question: str

@app.post("/ask")
def ask(req: AskQuestion):
    question = req.question
    matched_models = get_models(question)
    if len(matched_models) == 0:
        return {"message": "your query does not contain any model name. sorry!!! :("}
    elif len(matched_models) == 1:
        message = get_details_message(matched_models[0])
        return {"message": message}
    message = ask_LLM(question, matched_models)
    return {"message": message}


def get_models(question: str)->list[str]:
    question_lower = question.lower()
    con = get_db_connection()
    cur = con.cursor()

    cur.execute("SELECT model, release_date, display_size, display_width, display_height, battery, camera, ram, storage, price FROM phones")
    rows = cur.fetchall()
    cur.close()
    con.close()

    matched_phones = []

    for r in rows:
        model_name = r[0]
        model_words = model_name.lower().split()
        if all(word in question_lower for word in model_words):
            matched_phones.append({
                "model": r[0],
                "release_date": r[1],
                "display_size": r[2],
                "display_width": r[3],
                "display_height": r[4],
                "battery": r[5],
                "camera": r[6],
                "ram": r[7],
                "storage": r[8],
                "price": r[9]
            })
    return matched_phones
