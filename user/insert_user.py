import pymongo
import json


#connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["user"]
mycol = mydb["user"]

#insert user.json into mongodb
with open('user.json',encoding="utf-8") as f:
    file_data = json.load(f)
x = mycol.insert_many(file_data)
