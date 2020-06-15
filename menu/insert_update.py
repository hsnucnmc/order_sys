#!/usr/bin/env python3
import pymongo
import json
import base64

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["menu"]
mycol = mydb["menu"]

# data
name = "炒面"
price = 70
date = 20200614
with open("upload.jpg", "rb") as image:
    img_data = image.read()
    img_string = base64.encodebytes(img_data)

# dict
mydict = {
    "name": name,
    "price": price,
    "date": date,
    "image": img_string
}

# update if name = "炒面" & date = 20200614
x = mycol.update_one({"name": name, "date": date}, {'$set': mydict}, upsert=True)
# x = mycol.insert_one(mydict)
