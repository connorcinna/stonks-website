from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import get_historical_intraday
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from datetime import datetime

API_PUBLIC_KEY = 'pk_65b52176e67f4e8d86a61b3273d98107'
API_SECRET_KEY = 'sk_0df76468e959446e88abe99920684244'

date = datetime(2019, 10, 25)

data = get_historical_intraday('BYND', date, output_format='pandas', token = API_SECRET_KEY)

style.use('seaborn-bright')

y = []
x = []
count = 0
index = 0

for idx, row in data.iterrows():
    if not pd.isnull(row['average']):        
        plt.suptitle('BYND Stock on 10/25/2019')
        plt.xlabel('Time (Minute)')
        plt.ylabel('Price (Dollars)')
        y.append(row['average'])
        x.append(count)
        
        x_mask = x[index - 5: index + 5]
        y_mask = y[index - 5: index + 5]
        index += 1
        
        ax = plt.gca()

        # recompute the ax.dataLim
        ax.relim()
        # update ax.viewLim using the new dataLim
        ax.autoscale_view()
        
        plt.scatter(x_mask, y_mask, c='g')
        plt.pause(0.05)

    count += 1
        
plt.show()