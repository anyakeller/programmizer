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
            if req not in student["completedCourses"]:
#get course
                for coursekey in db:
                    if db[coursekey]["code"] == req: #if found course
                        for section in db[coursekey]["sections"]: #for each section try to register student
                            ans = register.enroll(student["id"],req,section["section"])
                            if ans == "Sucess":
                                print 'Course '+ str(req) + ' added to student ' + str(student['id'])
                                break
                            else:
                                print "Couldn't add " + str(req) + " to student " + str(student['id'])
                                if ans == 1:
                                    print "Error - student already enrolled in that class.  Moving on to next course to add."
                                    break
                                elif ans == 2:
                                    print "Error - student alredy registered that period.  Trying next section."
                                elif ans == 3:
                                    print "Error - course already taken by student.  Moving on to next course to add."
                                    break
                                else:
                                    print ans
                                    print "also IDK why but we're going to try to add them to the next section or whatever..."
                            ans = ""
programCourses()
