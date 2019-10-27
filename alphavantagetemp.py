from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import os
import time
#35G9GZ5H11ELL5WF
#SL5K4V6C43WBHMTB
companies = ['NCR','BLK','EFX','COF','ACN']
ts = TimeSeries(key='35G9GZ5H11ELL5WF', output_format='pandas') #key is api key from alpha vantage
count = 0
while(1):
    for company in companies:
        start_time = time.time() #keep tracks of how long this iteration is taking
        # Get json object with the intraday data and another with  the call's metadata
        #data, meta_data = ts.get_intraday(symbol=company,interval='1min',outputsize='compact')
        data, meta_data = ts.get_intraday(symbol=company,interval='60min',outputsize='compact')
        #data is a dictionary
        plt.figure()
        data['4. close'].plot()
        plt.title('Intraday Times Series for ' + company + ' stock (60 min interval)')
        plt.ylabel('US dollars ($)')    
        strFile = './stonksgraphs/%sgraph%s.png'%(company,str(count)) 
        if os.path.isfile(strFile):
            os.remove(strFile) #makes sure that old file is overwritten or else i lose a lot of space
        plt.savefig(strFile)
        plt.close()
        count += 1
    waiting = int(60.0-((time.time() - start_time) % 60.0))
    for i in range(waiting):
        print("Waiting to " + str(waiting) + ": " + str(i))
        time.sleep(1.0) #only make it sleep as long as it has to
        

