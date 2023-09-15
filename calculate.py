from get_keys import get_api_key
from datetime import datetime, timedelta
from get_all_trades import get_trades

# Get Binance api keys
api_key, secret = get_api_key()
# Get all trades
all_trades = get_trades()
# Choose time range
time_range = 365  # Time range in days

# Calculate profit, tax and commission from all trades
def calculate(all_trades, time_range):
    now = datetime.now()
    start_time = now - timedelta(days=time_range)
    profit = 0.0
    taxes = 0.0
    commission = 0.0
    for trade in all_trades:
        trade_time = datetime.fromtimestamp(trade['time'] / 1000)  # Convert Unix timestamp to datetime
        if trade_time >= start_time and trade_time <= now:
            profit += float(trade['realizedPnl'])  # Convert 'realizedPnl' to float
            taxes += float(trade['realizedPnl']) * 0.31  # Assuming tax rate is 31%
            commission += float(trade['commission'])
    return profit, taxes, commission


profit, taxes, commission = calculate(all_trades, time_range)
actual_profit = profit - taxes - commission

print(f"Profit: {profit:.2f} \n Taxes:  {taxes:.2f} \n Commission: {commission:.2f} \n Actual profit: {actual_profit:.2f}")
