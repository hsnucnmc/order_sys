import pymongo
import json
import base64

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["menu"]
mycol = mydb["menu"]

# data
name = "炒面"
date = 20200614

# filter
myquery = {"name": name, "date": date}

# delete
mycol.delete_one(myquery)
