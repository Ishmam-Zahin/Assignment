from TradingAnalyzer import TradingAnalyzer

def main():
    print("\n" + "=" * 50)
    print("📈 Welcome to Trading Analyzer! 📊")
    print("=" * 50 + "\n")
    
    name = input("🏢 Enter company ticker (e.g., AAPL, TSLA): ").upper()
    start_date = input("📅 Start date (yyyy-mm-dd): ")
    end_date = input("📅 End date (yyyy-mm-dd): ")
    
    print()
    analyzer = TradingAnalyzer(name, start_date, end_date)
    
    try:
        analyzer.fetch_data()
    except Exception as e:
        print(f"❌ Oops! Something went wrong: {e}")
        print("💡 Please check your ticker symbol and dates, then try again.\n")
        return
    
    analyzer.clean_data()
    analyzer.calculate_moving_averages()
    
    print("=" * 50)
    print("✅ Ready to simulate trades!")
    print("=" * 50 + "\n")
    
    while True:
        try:
            amount = float(input("💵 Enter starting amount (e.g., 5000) or -1 to exit: "))
            if amount == -1:
                break
            if amount <= 0:
                print("⚠️  Please enter a positive amount!\n")
                continue
            analyzer.start(amount)
        except ValueError:
            print("⚠️  Invalid input! Please enter a number.\n")
            continue
    
    print("\n" + "=" * 50)
    print("👋 Thanks for using Trading Analyzer!")
    print("🌟 Have a great day! Goodbye!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()