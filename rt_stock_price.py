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

assets = ['NCR', 'BLK', 'EFX', 'COF', 'ACN']
datasets = []
for asset in assets:
    datasets.append(get_historical_intraday(asset, date, output_format='pandas', token = API_SECRET_KEY))

style.use('seaborn-bright')

y = {}
x = {}
count = {}
index = {}

figs = {}
axs = {}
# We just need the idx.
for idx, _ in datasets[0].iterrows():
    for ind, data in enumerate(datasets):
        # Init dictionary entries to empty arrays.
        if ind not in y:
            y[ind] = []
        if ind not in x:
            x[ind] = []
        if ind not in count:
            count[ind] = 0
        if ind not in index:
            index[ind] = 0
        # Iterate through datasets.    
        row = data.loc[idx]
        if not pd.isnull(row['average']):        
            plt.suptitle(assets[ind] + ' Stock on ' + date.strftime('%m/%d/%Y'))
            plt.xlabel('Minutes from Market Open')
            plt.ylabel('Price (Dollars)')
            y[ind].append(row['average'])
            x[ind].append(count[ind])
            
            x_mask = x[ind][index[ind] - 5: index[ind] + 5]
            y_mask = y[ind][index[ind] - 5: index[ind] + 5]
            index[ind] += 1
            
            ax = plt.gca()

            # recompute the ax.dataLim
            ax.relim()
            # update ax.viewLim using the new dataLim
            ax.autoscale_view()
            
            plt.scatter(x_mask, y_mask, c='g')
            plt.pause(0.5)
        count[ind] += 1
        
plt.show()