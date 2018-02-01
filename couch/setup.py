import couchdb
couch = couchdb.Server()

def setupFreshCourses():
    courseNames = ["Freshman Comp","Algebra","Bio","Spanish","Frehsman Gym","World History"]
    db = couch.create('courses')
    '''
    codecount = 1
    roomcount = 1

    for name in courseNames:
        course = {
            "name": name,
            "code": codecount,
            "sections":[
                {"section":"a",'teacher':'asdf',"days":"MTWRF","period":1,"room":str(roomcount) ,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"b",'teacher':'asdf',"days":"MTWRF","period":2,"room":str(roomcount) + 1,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"c",'teacher':'asdf',"days":"MTWRF","period":3,"room":str(roomcount) + 2,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"d",'teacher':'asdf',"days":"MTWRF","period":4,"room":str(roomcount) + 3,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"e",'teacher':'asdf',"days":"MTWRF","period":5,"room":str(roomcount) + 4,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]},
                {"section":"f",'teacher':'asdf',"days":"MTWRF","period":6,"room":str(roomcount) + 5,"double":False,"capacity":30,"numRegistered":0,"sRegistered":[]}
            ]
        }
        codecount = codecount + 1
        roomcount = roomcount + 6
        db.save(course)
        '''
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
