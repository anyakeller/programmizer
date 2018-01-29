from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.simple

#format - each period is an individual entry (IK that's crazy)
'''
course = {
    "name": ,
    "code": ,
    "sections":[{
        "section": ,
        "days": ,
        "period": ,
        "room": ,
        "double": ,
        "capacity": ,
        "numRegistered": ,
        "sRegistered":
        }
    ]
}

#required courses
#numbers are course codes
reqs = {
    "freshman":[1,2,3,4,5,6],
    "sophomore":[7,8,9,10,11,12],
    "junior":[13,14,15,16,17,18],
    "senior":[19,20,21,22,23],
    "overall":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
}
'''

def setupFreshCourses():
    courseNames = ["Freshman Comp","Algebra","Bio","Spanish","Frehsman Gym","World History"]

    codecount = 1
    roomcount = 1

    for name in courseNames:
        course = {
            "name": name,
            "code": codecount,
            "sections":[
                {"section":"a","days":"MTWRF","period":1,"room":roomcount ,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"b","days":"MTWRF","period":2,"room":roomcount + 1,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"c","days":"MTWRF","period":3,"room":roomcount + 2,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]}
            ]
        }
        codecount = codecount + 1
        roomcount = roomcount + 3
        db.courses.insert_one(course)

setupFreshCourses()
print db.courses.find_one({'code': 4})

#student structure
#filled reqs, index of req filled in reqirement list
'''
student = {
    "id": ,
    "grade":,
    "filledReqs": [],
    "schedule":{
        "1":,
        "2":,
        "3":,
        "4":,
        "5":,
        "6":,
        "7":,
        "8":,
        "9":,
        "10":
    },
    "notes":
}
'''

def setupFreshmen():
    for i in range(1 , 20):
        student = {
            "id": i,
            "grade":"freshman",
            "filledReqs": [],
            "schedule":{
                "1":"",
                "2":"",
                "3":"",
                "4":"",
                "5":"",
                "6":"",
                "7":"",
                "8":"",
                "9":"",
                "10":""
            },
            "notes":"n/a"
        }
        db.students.insert_one(student)
setupFreshmen()




