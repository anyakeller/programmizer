import pprint
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.simple4

#required courses
reqs = {
    "freshman":[1,2,3,4,5,6],
    "sophomore":[7,8,9,10,11,12],
    "junior":[13,14,15,16,17,18],
    "senior":[19,20,21,22,23],
    "overall":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
}

#show classes
def showClasses():
    for doc in db.courses.find():
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(doc)
#showClasses()

#place student in class (student id, course code, and section)
def enroll(sid,code,section):
    #get course
    course = db.courses.find_one({'code':code})
    #get student
    student = db.students.find_one({'id':sid})
    count = 0
    for sec in course["sections"]:
        if sec["section"] == section:
            #check if class has room
            if sec["capacity"] == sec["numRegistered"]:
                return "Error Max Capacity"
            if student["schedule"][str(sec["period"])] != "":
                return "Error Student already enrolled that period"
            if sid in sec["sRegistered"]:
                return "Error Student already enrolled in that class"
            else: #enroll the student
                sections = course["sections"]
                sections [count]["numRegistered"] = sections[count]["numRegistered"] + 1
                sections[count]["sRegistered"].append(sid)
                db.courses.update_one({'code': code}, {"$set":{"sections": sections}})
                schedule = student["schedule"]
                schedule[str(sections[count]["period"])] = str(code) + "-" + section
                db.students.update_one({'id': sid}, {"$set":{"schedule": schedule}})
                filled = student["filledReqs"]
                if code in reqs["overall"]:
                    filled.append(code)
                    db.students.update_one({'id':sid},{"$set":{"filledReqs":filled}})
                return "Course added"

        count = count + 1


#test
def testEnroll():
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(db.students.find_one({'id':1}))

    pp.pprint(db.courses.find_one({'code':1}))

    print enroll(1,1,"a")
    print "after================================="
    pp.pprint(db.students.find_one({'id':1}))

    pp.pprint(db.courses.find_one({'code':1}))
testEnroll()
