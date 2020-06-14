import pymongo
import json

#connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["user"]
mycol = mydb["user"]

myquery = { "_id" : 710598 }

mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)


