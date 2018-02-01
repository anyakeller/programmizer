import couchdb
import register
couch = couchdb.Server()


reqs = {
    'freshman':[1,2,3,4,5,6],
    'sophomore':[7,8,9,10,11,12],
    'junior':[13,14,15,16,17,18],
    'senior':[19,20,21,22,23],
    'all':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,7,18,19,20,21,22,23]
    }

def programCourses():
    dbs = couch["students"] #student db
    db = couch["courses"] #student db
    for key in dbs:
        student = dbs[key]
        print 'Scheduling student ' + str(student["id"])
        studentreqs = reqs[student['grade']]
        studentreqs = studentreqs + student["additionalReqs"]
        print 'reqs needed ' + str(studentreqs)
        for req in studentreqs:
            if req not in student["filledReqs"]:
#get course
                for coursekey in db:
                    if db[coursekey]["code"] == req:
                        for section in db[coursekey]["sections"]:
                            try:
                                ans = register.enroll(student["id"],req,section["section"])
                                if ans:
                                    print 'Course '+ str(req) + ' added to student ' + str(student['id'])
                                    break
                                else:
                                    print "Couldn't add " + str(req) + " to student " + str(student['id'])
                                    print 'student already enrolled that period'
                            except:
                                print "section full, trying next section..."
                    ans = ""
programCourses()
