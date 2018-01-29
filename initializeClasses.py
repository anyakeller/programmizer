from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.classes

#format - each period is an individual entry (IK that's crazy)
'''
course = {
    "name": ,
    "code": ,
    "section": ,
    "day": ,
    "period": ,
    "room": ,
    "capacity": ,
    "isDouble": ,
    "numRegistered": ,
    "sRegistered":
    }
'''

course = {
    "name": "Mandarin ii 1 of 2",
    "code": "FMS63",
    "section": "1002",
    "day": "MTWRF",
    "period": 2,
    "room": 1033,
    "capacity": 20,
    "isDouble": False,
    "numRegistered": 10,
    "sRegistered": [1,2,3,4,5,6,7,8,9,10]
    }
db.classes.insert_one(course)
course = {
    "name": "Technical Graphic Communications",
    "code": "TDS11",
    "section": "1005",
    "day": "MTWRF",
    "period": 3,
    "room": 1007,
    "capacity": 20,
    "isDouble": False,
    "numRegistered": 10,
    "sRegistered": [1,2,3,4,5,6,7,8,9,10]
    }
db.classes.insert_one(course)
print db.classes.find_one({"name": "Mandarin ii 1 of 2"})

