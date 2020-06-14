import pymongo
import json

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["menu"]
mycol = mydb["menu"]

# filter
name = "炒面"
date = 20200614

# query
myquery = {"name": name, "date": date}
mydoc = mycol.find(myquery)

# save result in result.txt
with open("result.txt", "w") as query_result:
    for x in mydoc:
        query_result.write(str(x).replace("\\n", ''))
