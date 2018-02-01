import couchdb
couch = couchdb.Server()

def setupFreshCourses():
    courseNames = ["Freshman Comp","Algebra","Bio","Spanish","Frehsman Gym","World History"]
    db = couch.create('courses')
    codecount = 1
    roomcount = 1

    for name in courseNames:
        course = {
            "name": name,
            "code": codecount,
            "sections":[
                {"section":"a","days":"MTWRF","period":1,"room":roomcount ,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"b","days":"MTWRF","period":2,"room":roomcount + 1,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"c","days":"MTWRF","period":3,"room":roomcount + 2,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"d","days":"MTWRF","period":4,"room":roomcount + 3,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"e","days":"MTWRF","period":5,"room":roomcount + 4,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"f","days":"MTWRF","period":6,"room":roomcount + 5,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]}
            ]
        }
        codecount = codecount + 1
        roomcount = roomcount + 6
        db.save(course)

setupFreshCourses()

def displayFreshCourses():
    if "courses" in couch:
        db = couch["courses"]
        for doc in db:
            print db[doc]
#displayFreshCourses()


def setupFreshmen():
    db = couch.create('students')
    for i in range(1,20):
        student = {
            "id":i,
            "grade":"freshman",
            "additionalReqs":[4], #ie mando for this year
            "completedCourses":[],
            "schedule":{
                '1':'',
                '2':'',
                '3':'',
                '4':'',
                '5':'',
                '6':'',
                '7':'',
                '8':'',
                '9':'',
                '10':''
            },
            "notes":"n/a"
        }
        db.save(student)
setupFreshmen()

def displayFreshmen():
    if "students" in couch:
        db = couch["students"]
        for doc in db:
            print db[doc]
#displayFreshmen()
