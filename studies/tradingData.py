## scrapping volume data from ftx perpetuals

import studiesLib
import sys
import redis

# get redis access data and creating a connection object
[host,port,pw] = studiesLib.getDataFromJson('keyData.json')['concentrador']
redDb = redis.Redis(host=host, port=port, db=0,password=pw,decode_responses=True)