from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import os
import time

companies = ['NCR','GOOGL','FB','AMZN','MSFT']
ts = TimeSeries(key='SL5K4V6C43WBHMTB', output_format='pandas') #key is api key from alpha vantage
count = 0
while(1):
    for company in companies:
        start_time = time.time() #keep tracks of how long this iteration is taking
        # Get json object with the intraday data and another with  the call's metadata
        data, meta_data = ts.get_intraday(symbol=company)
        #data is a dictionary
        plt.figure()
        data['4. close'].plot()
        #fig = plt.figure()
        plt.title('Intraday Times Series for ' + company + ' stock')
        plt.ylabel('US dollars ($)')    
        strFile = './stonks/%sgraph.png'%(company) 
        if os.path.isfile(strFile):
            os.remove(strFile) #makes sure that old file is overwritten or else i lose a lot of space
        plt.savefig(strFile)
        plt.close()
    waiting = int(60.0-((time.time() - start_time) % 60.0))
    for i in range(waiting):
        print("Waiting to " + str(waiting) + ": " + str(i))
        time.sleep(1.0) #only make it sleep as long as it has to
        
#okay but bad news is 500 api calls per day and only 5 per minute
#also not plotting anying to the images being made
#i think we can get past this by getting a new api key every so often with a throwaway email address from
#totally going to put that picture of the stonks guy as the floor or something

