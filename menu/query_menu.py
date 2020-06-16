#!/usr/bin/env python3
import pymongo
import json
import base64

#connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["menu"]
mycol = mydb["menu"]

myquery = { "name" : "炒面" }
mydoc = mycol.find(myquery)
init_db=""
for x in mydoc:
    init_db += str(x)
database=init_db.split("\'image\':")[0]+init_db.split("\'image\': b\'")[1].split("\', \'")[1]
print(database)
image=base64.decodebytes(init_db.split("\'image\': b\'")[1].split("\', \'")[0].replace("\\n","").encode("UTF-8"))
image_result = open('decode.jpg', 'wb')
image_result.write(image)
