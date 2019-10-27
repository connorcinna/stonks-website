from alphavantage.price_history import (
  AdjustedPriceHistory, get_results, PriceHistory, IntradayPriceHistory,
  filter_dividends
)
import matplotlib.pyplot as plt
import os
import time
companies = ['NCR','BLK','EFX','COF','ACN']
count = 0
while(1):
    for company in companies:
        start_time = time.time() #keep tracks of how long this iteration is taking
        history = PriceHistory(period='W', output_size='compact')
        results = history.get(company)
        results.plot()
        plt.show()
        count += 1
    waiting = int(60.0-((time.time() - start_time) % 60.0))
    for i in range(waiting):
        print("Waiting to " + str(waiting) + ": " + str(i))
        time.sleep(1.0) #only make it sleep as long as it has to
        

