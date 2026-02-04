import requests

url = "http://127.0.0.1:8000/ask"

def main():
    print("✨ Welcome! How can I assist you today?\n")
    
    while True:
        prompt = input("💬 You(type exit to exit.): ")
        
        if prompt.lower() == "exit":
            break
        
        payload = {"question": prompt}
        print("⏳ Thinking...")
        
        response = requests.post(url, json=payload)
        
        if response.status_code >= 300:
            print("❌ Oops! Something went wrong. Please try again.\n")
            continue
        
        data = response.json()
        print(f"🤖 Assistant: {data['message']}\n")
    
    print("👋 Have a great day! Goodbye!\n")

if __name__ == "__main__":
    main()