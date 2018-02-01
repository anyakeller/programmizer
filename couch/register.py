import couchdb
couch = couchdb.Server()

reqs = {
    'freshman':[1,2,3,5,6],
    'sophomore':[7,8,9,10,11,12],
    'junior':[13,14,15,16,17,18],
    'senior':[19,20,21,22,23],
    'all':[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,1,7,18,19,20,21,22,23]
    }


def displayFreshCourses():
    if "courses" in couch:
        db = couch["courses"]
        for doc in db:
            print db[doc]["code"]
#displayFreshCourses()

def enroll(sid,code,section):
    db = couch["courses"]
    _id = 0
    for doc in db:
        if db[doc]['code'] == code:
            _id = doc
    course = db[_id]

    dbs = couch["students"]
    _id = 0
    for doc in dbs:
        if dbs[doc]['id'] == sid:
            _id = doc
    student = dbs[_id]

    count = 0
    for sec in course["sections"]:
        if course["sections"][count]["section"] == section:
            if sec["capacity"] == sec["numRegistered"]:
                return "Error - Class full"
            elif  sid in sec["sRegistered"]:
                return "Error - Student already in that class"
            elif student["schedule"][str(sec["period"])] != '': #if they're taking a course that period
                return "Error - already registered that period"
            elif code in student["completedCourses"]:  #if they already have that req filled
                return "Error - class already taken"
            else:
                course["sections"][count]["numRegistered"] = course["sections"][count]["numRegistered"] + 1
                course["sections"][count]["sRegistered"].append(sid)

                #enroll student
                student["schedule"][str(course["sections"][count]["period"])] = str(code) + "-" + section
                student["completedCourses"].append(code)
                db.save(course)
                dbs.save(student)
                return "Sucess"
        count = count + 1
    return "Error - Registration failed"
#print enroll(1,4,"a")

def deenroll(sid,pd):

    dbs = couch["students"]
    _id = 0
    for doc in dbs:
        if dbs[doc]['id'] == sid:
            _id = doc
    student = dbs[_id]

    if not student["schedule"][str(pd)]:
        return "Error - Student not enrolled that period"
    else:
        fullcode = student["schedule"][str(pd)].split("-")
        code = fullcode[0]
        db = couch["courses"]
        _id = 0
        for doc in db:
            if db[doc]['code'] == int(code):
                _id = doc
        course = db[_id]

        #remove student from course
        count = 0
        for sec in course["sections"]:
            if sec["section"] == fullcode[1]:
                course["sections"][count]["numRegistered"] = sec["numRegistered"] - 1
                index = sec["sRegistered"].index(sid)
                del course["sections"][count]["sRegistered"][index]
                db.save(course)
                break
            count = count + 1
        student["schedule"][str(pd)] = ""
        index = student["completedCourses"].index(int(code))
        del student["completedCourses"][index]
        dbs.save(student)
        return "Deenroll sucess"

    return "Error - Deenroll failled"
#print deenroll(1,1)
