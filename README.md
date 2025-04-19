### 📌 Objective:
Build a machine learning or statistical model that predicts daily peak electricity demand in Nepal. The model uses historical data and external factors like:

- Previous peak demand values
- Time of day / day of week / season
- Weather data (temperature, humidity, rainfall)
- Holiday calendar / special events
- Generation trends


### 🔍 Why it matters:
Peak demand is when electricity usage is at its highest—if NEA doesn't plan properly, it may:

- Fail to meet demand (leading to blackouts)
- Overproduce electricity (wasting resources)
- Miss optimal import/export opportunities

### 🧠 How it helps NEA:
- Better planning of NEA for power generation
- Optimize imports from India (only when needed)
- Export surplus energy to India when generation exceeds forecasted demand
- Reduce cost by avoiding last-minute decisions
- Improve grid reliability by avoiding overloads

### 🛠️ Tech stack & approach:
- Data sources: [NEA reports] (https://www.nea.org.np/dailyOperationalReports) 
- Libraries: pandas, scikit-learn
- Model: Time series forecasting (ARIMA)
- Output: Daily/hourly peak demand values 
