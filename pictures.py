import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
from get_keys import get_api_key
from get_all_trades import get_trades

api_key, secret = get_api_key()
all_trades = get_trades()

# Choose range in days
time_ranges = list(np.arange(1, 90))

profits = []
taxes = []
commissions = []
actual_profits = []

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


# Create a line graph to visualize the realized profit across time ranges
plt.plot(time_ranges, profits, marker='o', label='Realized Profit')
plt.plot(time_ranges, actual_profits, marker='o', label='Actual Profit (after taxes)')
plt.plot(time_ranges, commissions, marker='o', label='Commission')
plt.plot(time_ranges, taxes, marker='o', label='Taxes 20%')

plt.xlabel('Time Range (days)')
plt.ylabel('Value (in USDT)')
plt.title('Financial Metrics Over Time Ranges')
plt.legend()
plt.grid(True)

# Save the chart as an image
plt.savefig('financial_metrics_line_chart.png')

# Show the chart
plt.show()
