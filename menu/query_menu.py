#!/usr/bin/env python3
import pymongo
import json
import base64

#connect to mongodb
myclient = pymongo.MongoClient("mongodb://root:cnmc@140.131.149.39:465")
mydb = myclient["menu"]
mycol = mydb["menu"]

myquery = { "name" : "炒面" }
mydoc = mycol.find()
init_db=""
database=""
name=[]
for x in mydoc:
    init_db += str(x)
#print(init_db)
count=0
for y in init_db.split("}{"):
	count+=1
	database+=str(y).split("\'image\':")[0]
	name.append(str(y).split("\'image\':")[0].split("\'name\':")[1].replace("\'","").replace(' ',"").replace(',',"")+".jpg")
	database+=str(y).split("\'image\': b\'")[1].split("\', \'")[1]
	if count<len(init_db.split("}{")):
		database+="}{"
	image=base64.decodebytes(init_db.split("\'image\': b\'")[1].split("\', \'")[0].replace("\\n","").encode("UTF-8"))
	image_result = open(name[count-1], 'wb')
	image_result.write(image)
print(database)
