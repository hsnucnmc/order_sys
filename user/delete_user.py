import pymongo
import json


#connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["user"]
mycol = mydb["user"]

myquery = { "grade": 108 }
x = mycol.delete_many(myquery)
