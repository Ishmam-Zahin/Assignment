import yfinance as yf
import pandas as pd

class TradingAnalyzer:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
    
    def start(self, amount):
        df = self.data_frame
        inHand = amount
        inPosition = False
        totalShares = 0
        buyPrice = 0
        
        print(f"\n🚀 Starting trading simulation with ${amount:,.2f}\n")
        
        for index, row in df.iterrows():
            ma50 = row["MovAvg50"]
            ma200 = row["MovAvg200"]
            closeMoney = row["Close"]
            
            if pd.isna(ma50) or pd.isna(ma200) or pd.isna(closeMoney):
                continue
            
            if (ma50 > ma200) and not inPosition:
                totalShares = int(inHand / closeMoney)
                if totalShares == 0:
                    continue
                
                totalCost = closeMoney * totalShares
                buyPrice = closeMoney
                inHand = inHand - totalCost
                inPosition = True
                print(f"📈 BUY on {index.date()}")
                print(f"   Shares: {totalShares} @ ${closeMoney:.2f} each")
                print(f"   Total invested: ${totalCost:,.2f}")
                print(f"   Cash remaining: ${inHand:,.2f}\n")
                
            elif (ma50 < ma200) and inPosition:
                inPosition = False
                totalGain = totalShares * closeMoney
                profit = (closeMoney - buyPrice) * totalShares
                profitPercent = ((closeMoney - buyPrice) / buyPrice) * 100
                inHand += totalGain
                
                if profit >= 0:
                    print(f"📉 SELL on {index.date()}")
                    print(f"   Shares: {totalShares} @ ${closeMoney:.2f} each")
                    print(f"   Total received: ${totalGain:,.2f}")
                    print(f"   💰 Profit: ${profit:,.2f} ({profitPercent:+.2f}%)")
                    print(f"   Cash in hand: ${inHand:,.2f}\n")
                else:
                    print(f"📉 SELL on {index.date()}")
                    print(f"   Shares: {totalShares} @ ${closeMoney:.2f} each")
                    print(f"   Total received: ${totalGain:,.2f}")
                    print(f"   📉 Loss: ${profit:,.2f} ({profitPercent:+.2f}%)")
                    print(f"   Cash in hand: ${inHand:,.2f}\n")
                
                totalShares = 0
        
        if inPosition:
            inPosition = False
            closeMoney = row["Close"]
            totalGain = totalShares * closeMoney
            profit = (closeMoney - buyPrice) * totalShares
            profitPercent = ((closeMoney - buyPrice) / buyPrice) * 100
            inHand += totalGain
            
            print(f"📉 FINAL SELL on {index.date()} (closing position)")
            print(f"   Shares: {totalShares} @ ${closeMoney:.2f} each")
            print(f"   Total received: ${totalGain:,.2f}")
            if profit >= 0:
                print(f"   💰 Profit: ${profit:,.2f} ({profitPercent:+.2f}%)")
            else:
                print(f"   📉 Loss: ${profit:,.2f} ({profitPercent:+.2f}%)")
            print(f"   Cash in hand: ${inHand:,.2f}\n")
            
            totalShares = 0
        
        finalProfit = inHand - amount
        finalPercent = (finalProfit / amount) * 100
        
        print("=" * 50)
        print("📊 TRADING SUMMARY")
        print("=" * 50)
        print(f"💵 Starting capital:  ${amount:,.2f}")
        print(f"💰 Ending balance:    ${inHand:,.2f}")
        print("-" * 50)
        if finalProfit >= 0:
            print(f"✅ Total profit:      ${finalProfit:,.2f} ({finalPercent:+.2f}%)")
            print("🎉 Great job! You made money!")
        else:
            print(f"❌ Total loss:        ${finalProfit:,.2f} ({finalPercent:+.2f}%)")
            print("😔 Better luck next time!")
        print("=" * 50 + "\n")
    
    def calculate_moving_averages(self):
        self.data_frame["MovAvg50"] = self.data_frame["Close"].rolling(window=50).mean()
        self.data_frame["MovAvg200"] = self.data_frame["Close"].rolling(window=200).mean()
    
    def clean_data(self):
        print("\n🧹 Cleaning data...")
        print(f"   Duplicates found: {self.data_frame.duplicated().sum()}")
        print(f"   NaN values found:\n{self.data_frame.isna().sum()}")
        
        self.data_frame = self.data_frame.drop_duplicates()
        self.data_frame = self.data_frame.ffill()
        self.data_frame = self.data_frame.dropna()
        
        print(f"✨ Data cleaned successfully! Shape: {self.data_frame.shape}\n")
    
    def fetch_data(self):
        print(f"📥 Fetching data for {self.name} from {self.start_date} to {self.end_date}...")
        self.data_frame = yf.download(self.name, self.start_date, self.end_date)
        
        if self.data_frame.empty:
            raise ValueError("❌ No data found!")
        
        self.data_frame.columns = self.data_frame.columns.get_level_values(0)
        print("✅ Data fetched successfully!\n")