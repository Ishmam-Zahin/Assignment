# 📊 Algorithmic Trading & AI Phone Advisor

A dual-project repository featuring an **Algorithmic Trading Simulator** and a **Samsung Phone AI Advisor** with RAG-based retrieval and LLM-powered recommendations.

---

## 🎥 Video Demonstration

📹 **Watch the demo:** [Google Drive Video Link](YOUR_GOOGLE_DRIVE_LINK_HERE)

---

## 📑 Table of Contents

- [Task 1: Algorithmic Trading Analyzer](#task-1-algorithmic-trading-analyzer)
- [Task 2: Samsung Phone AI Advisor](#task-2-samsung-phone-ai-advisor)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Task 1: Algorithmic Trading Analyzer

### 📖 Overview

An algorithmic trading simulator that uses the **Golden Cross** strategy (50-day and 200-day moving averages) to make buy/sell decisions. The tool downloads historical stock data, analyzes trends, and simulates trading with a given budget.

### ✨ Features

- 📈 Historical stock data fetching using Yahoo Finance
- 🧹 Automatic data cleaning (duplicates, NaN handling)
- 📊 Moving average calculation (50-day and 200-day)
- 💰 Golden Cross trading strategy implementation
- 📉 Profit/loss tracking for each trade
- 🎯 Final portfolio summary with performance metrics

### 🛠️ Technologies Used

- **Python 3.x**
- **yfinance** - Stock data retrieval
- **pandas** - Data manipulation and analysis

### 📂 Project Structure

```
task1/
├── TradingAnalyzer.py    # Main trading logic class
├── user.py               # User interface for interaction
└── README.md             # Documentation
```

### 🔧 Installation

1. Navigate to the task1 directory:

```bash
cd task1
```

2. Install required dependencies:

```bash
pip install yfinance pandas
```

### ▶️ How to Run

1. Navigate to the task1 directory:

```bash
cd task1
```

2. Run the program:

```bash
python user.py
```

3. Follow the prompts:
   - Enter company ticker symbol (e.g., AAPL, TSLA, GOOGL)
   - Enter start date (format: yyyy-mm-dd)
   - Enter end date (format: yyyy-mm-dd)
   - Enter starting amount for simulation (e.g., 5000)
   - Enter -1 to exit the simulation

### 💡 Example Usage

```
🏢 Enter company ticker (e.g., AAPL, TSLA): AAPL
📅 Start date (yyyy-mm-dd): 2018-01-01
📅 End date (yyyy-mm-dd): 2023-12-31
💵 Enter starting amount (e.g., 5000) or -1 to exit: 5000

🚀 Starting trading simulation with $5,000.00

📈 BUY on 2018-04-12
   Shares: 25 @ $170.05 each
   Total invested: $4,251.25
   Cash remaining: $748.75

📉 SELL on 2018-11-15
   Shares: 25 @ $186.80 each
   Total received: $4,670.00
   💰 Profit: $418.75 (+9.84%)
   Cash in hand: $5,418.75

...
```

---

## 🤖 Task 2: Samsung Phone AI Advisor

### 📖 Overview

An intelligent AI assistant that helps users make informed decisions when buying Samsung smartphones. The system combines **RAG (Retrieval-Augmented Generation)** with **LLM-powered analysis** to provide specifications, comparisons, and recommendations.

### ✨ Features

- 🔍 Natural language query processing
- 📱 Detailed phone specifications retrieval
- 🆚 Intelligent phone comparisons
- 💡 Smart recommendations based on user needs
- 🗄️ PostgreSQL database for structured data storage
- 🧠 LLM-powered response generation via OpenRouter
- ⚡ FastAPI backend for efficient API handling

### 🛠️ Technologies Used

- **Python 3.x**
- **FastAPI** - Backend API framework
- **PostgreSQL** - Database for phone specifications
- **OpenAI SDK** - LLM integration via OpenRouter
- **psycopg2** - PostgreSQL adapter
- **python-dotenv** - Environment variable management
- **BeautifulSoup** / **Scrapy** - Web scraping (GSMArena)

### 📂 Project Structure

```
task2/
├── backend/
│   ├── main.py           # FastAPI backend server
│   ├── dbingest.py       # Database ingestion script
│   ├── .env.example      # Environment variables template
│   └── requirements.txt  # Backend dependencies
├── ai_assistant.py       # User interface client
└── README.md             # Documentation
```

### 🔧 Installation

1. Navigate to the task2 directory:

```bash
cd task2
```

2. Install backend dependencies:

```bash
cd backend
pip install fastapi uvicorn psycopg2-binary openai python-dotenv pydantic
```

3. Install client dependencies:

```bash
cd ..
pip install requests
```

### ⚙️ Configuration

1. Create a `.env` file in the `backend/` folder:

```bash
cd backend
cp .env.example .env
```

2. Add your configuration to `.env`:

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=samsung_phones
DB_USER=your_username
DB_PASSWORD=your_password

# OpenRouter API Configuration
LLM_API=your_openrouter_api_key
```

3. **Get OpenRouter API Key:**
   - Visit [OpenRouter](https://openrouter.ai/)
   - Sign up for a free account
   - Generate an API key from your dashboard

4. **Set up PostgreSQL Database:**
   - Install PostgreSQL on your system
   - Create a database named `samsung_phones`
   - Update the `.env` file with your credentials

### 📥 Database Setup

1. Navigate to the backend folder:

```bash
cd backend
```

2. Run the database ingestion script:

```bash
python dbingest.py
```

This will:

- Create the necessary tables in PostgreSQL
- Scrape Samsung phone data from GSMArena
- Insert 20-30 Samsung phone models into the database

### ▶️ How to Run

1. **Start the Backend Server:**

```bash
cd task2/backend
uvicorn main:app --reload
```

The backend will start at `http://127.0.0.1:8000`

2. **Run the AI Assistant (in a new terminal):**

```bash
cd task2
python ai_assistant.py
```

3. **Interact with the assistant:**
   - Ask questions about Samsung phones
   - Compare different models
   - Get recommendations based on your needs
   - Type `exit` to quit

### 💡 Example Usage

```
✨ Welcome! How can I assist you today?

💬 You(type exit to exit.): What are the specs of Samsung Galaxy S23 Ultra?
⏳ Thinking...
🤖 Assistant: Details for model 'Samsung Galaxy S23 Ultra' are given below:
- release date: 2023-02-01
- display size: 6.8inch
- display resolution: 1440 x 3088
- battery: 5000mph
- camera: 200MP
- memory: 12GB
- storage: 256GB
- price: $1199

💬 You(type exit to exit.): Compare Galaxy S23 Ultra and S22 Ultra
⏳ Thinking...
🤖 Assistant: The Samsung Galaxy S23 Ultra offers improvements over the S22 Ultra
with a 200MP camera (vs 108MP), better battery optimization, and a newer processor.
Display sizes are similar at 6.8 inches. For photography and long-term performance,
the S23 Ultra is recommended, though the S22 Ultra remains a strong value option.

💬 You(type exit to exit.): Which Samsung phone has the best battery under $1000?
⏳ Thinking...
🤖 Assistant: The Samsung Galaxy M54 5G offers the best battery under $1000 with
a 6000mAh capacity, priced at $449. It provides excellent battery life for heavy
users while staying well within budget.

💬 You(type exit to exit.): exit
👋 Have a great day! Goodbye!
```

### ⚠️ Important Notes

- **OpenRouter Free API:** The free tier models can be slower. Please be patient while waiting for responses.
- **Alternative Models:** You can switch to different models by updating the `LLM_MODEL` variable in `backend/main.py`
- **Rate Limits:** Free tier APIs may have rate limits. Consider upgrading for production use.

### 🔌 API Endpoints

**Base URL:** `http://127.0.0.1:8000`

#### `POST /ask`

Ask questions about Samsung phones.

**Request Body:**

```json
{
  "question": "Compare Samsung Galaxy S23 Ultra and S22 Ultra"
}
```

**Response:**

```json
{
  "message": "Samsung Galaxy S23 Ultra has better camera and battery life than S22 Ultra. Display is similar. Overall, S23 Ultra is recommended for photography and long usage."
}
```

---

## 📁 Project Structure

```
.
├── task1/
│   ├── TradingAnalyzer.py
│   ├── user.py
│   └── README.md
├── task2/
│   ├── backend/
│   │   ├── main.py
│   │   ├── dbingest.py
│   │   ├── .env.example
│   │   └── requirements.txt
│   ├── ai_assistant.py
│   └── README.md
└── README.md (this file)
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Yahoo Finance API for stock data
- GSMArena for phone specifications
- OpenRouter for LLM API access
- FastAPI for the excellent web framework

---

**Made with ❤️ and Python**
