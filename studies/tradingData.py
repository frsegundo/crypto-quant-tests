## scrapping volume data from ftx perpetuals

import studiesLib
import redis
import json
import pandas
import plotly.express as px

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
for dict_tmp in ftxData:
    ticker = dict_tmp['name']
    volumeUsd24h = dict_tmp['volumeUsd24h']
    if (volumeUsd24h > minimum_daily_volume) and (ticker not in not_interested_in) and ('/' not in ticker):  # the '/' will take spot out
        if '-PERP' in ticker:
            # take out the -PERP to make the x-axe plot more easy to be seen
            # so, when we read BTC, it will be BTC-PERP
            [prefix,postfix] = ticker.split('-')
            if prefix == 'PERP': print(ticker)
            ticker = prefix
        y_data.append(volumeUsd24h)
        x_data.append(ticker)

# creating a dataframe to work with
df_data = pandas.DataFrame({'ticker': x_data, 'volumeUsd24h': y_data})
colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c']

fig = px.treemap(data_frame=df_data,path=['ticker'],values='volumeUsd24h',title='Derivative Instruments with USD Volume > 10 M')
fig.update_traces(root_color="lightgrey")
fig.update_layout(
    treemapcolorway = colors, #defines the colors in the treemap
    margin = dict(t=50, l=25, r=25, b=25))
fig.show()