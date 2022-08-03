## scrapping volume data from ftx perpetuals

import studiesLib
import sys
import redis
import json
import pandas
import seaborn as sns
import matplotlib.pyplot as plt

# get redis access data and creating a connection object
[host,port,pw] = studiesLib.getDataFromJson('keyData.json')['concentrador']
redDb = redis.Redis(host=host, port=port, db=0,password=pw,decode_responses=True)

# access to data inside redis
ftxData = redDb.get('ftx_alt7:ftxmarkets')
ftxData = json.loads(ftxData)
ftxData = ftxData['content']['content']

# filtering data
minimum_daily_volume = 10*(10**6)
not_interested_in = ['USDT-PERP','USDT/USD']
y_data = []
x_data = []
for dict in ftxData:
    ticker = dict['name']
    volumeUsd24h = dict['volumeUsd24h']
    if (volumeUsd24h > minimum_daily_volume) and ticker not in not_interested_in:
        if '-PERP' in ticker:
            # take out the -PERP to make the x-axe plot more easy to be seen
            # so, when we read BTC, it will be BTC-PERP
            [prefix,postfix] = ticker.split('-')
            ticker = prefix
        y_data.append(volumeUsd24h)
        x_data.append(ticker)

# creating a dataframe to work with
df_data = pandas.DataFrame({'ticker': x_data, 'volumeUsd24h': y_data})
df_data.sort_values(by=['volumeUsd24h'],inplace=True)

# plotting data in a bar chart
sns.barplot(x = 'ticker',y = 'volumeUsd24h',data = df_data)
plt.show()
