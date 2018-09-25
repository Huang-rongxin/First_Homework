#coding=utf-8
import pymongo
from pymongo import MongoClient

client= MongoClient('mongodb://localhost:27017/')

db = client.test

my_set = db.user


#my_set.insert({"name":"黄容鑫","age":20,"sex":"男","id":"1715080119"})
#my_set.insert({"name":"庞家俊","age":22,"sex":"男","id":"1715080117"})
#my_set.insert({"name":"李维杰","age":20,"sex":"男","id":"1715080113"})
#my_set.insert({"name":"黄伟刚","age":21,"sex":"男","id":"1715080108"})
#my_set.insert({"name":"白雪","age":19,"sex":"女","id":"1715080130"})
#my_set.insert({"name":"吴欢","age":19,"sex":"男","id":"1715080111"})

my_set.remove({"name": "白雪"})

my_set.update({"name":"黄容鑫"},{'$set':{"age":21}})

for i in my_set.find({"sex":"男"}):
    print(i)
print("\n")

for i in my_set.find({"age": {"$gt": 19}}):
    print(i)
