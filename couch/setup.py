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
                {"section":"c","days":"MTWRF","period":3,"room":roomcount + 2,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]}
            ]
        }
        codecount = codecount + 1
        roomcount = roomcount + 3
        db.save(course)
    for ids in db :
        print ids

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
            "filledReqs":[],
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
