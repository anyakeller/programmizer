import couchdb
couch = couchdb.Server()
def iscodeTaken(code):
    db = couch["courses"]
    for courseid in db:
        if db[courseid]['code'] == code:
            return True
    return False

def suggestCode(n):
    db = couch["courses"]
    count = n
    for courseid in db:
        if count  <  db[courseid]["code"]:
            count = db[courseid]["code"]
    count = count + 1
    if not iscodeTaken(count):
        return count
    else:
        return suggestCode(count)

#print suggestCode(1)

def doesexsistbyname(name):
    db = couch["courses"]
    for courseid in db:
        if db[courseid]["name"] == name:
            return True
    return False

def doesexsistbycode(code):
    db = couch["courses"]
    for courseid in db:
        if db[courseid]["code"] == code:
            return True
    return False

def doesexsist(name,code):
    if doesexsistbyname(name):
        print "Name taken"
        return True
    if doesexsistbycode(code): #if either are true then it does exsist
        print "Code taken"
        print "Suggested Code: " + str(suggestCode(code))
        return True
    print 'Class does not exsist.  Yet...'
    return False
#doesexsist("Freshman Comp",999)
#doesexsist("Freshman",1)
#doesexsist("Freshman",999)

#create a course
def newCourse(name,code):
    if doesexsist(name,code):
        print "Course with same name or code already exsists"
    else:
        db = couch["courses"]
        course = {
                'name': name,
                'code':code,
                'sections':[]
                }
        db.save(course)
        print "Course " + name  + " created"
#newCourse("Freshman Comp",1)
def userNewCourse():
    name = raw_input("Course Name: ")
    code = input("Code: ")
    newCourse(name,code)

def doesSectionExsist(code,sectioncode):
    db = couch["courses"]
    for courseid in db:
        for section in db[courseid]["sections"]:
            if section["section"] == sectioncode:
                return True
    return False
#print doesSectionExsist(1,'x')

def newSection(code,sectioncode,days,period,room,double,capacity,numRegistered,sRegistered,teacher):
    if doesSectionExsist(code,sectioncode):
        print "Section code already used.  Check database to decide new section code."
    else:
        newSection = {
                'section':sectioncode,
                'teacher':teacher,
                'days':days,
                'period':period,
                'room':room,
                'double':double,
                'capacity':capacity,
                'numRegistered':numRegistered,
                'sRegistered':sRegistered
                }
        db = couch["courses"]
        #find course
        for courseid in db:
            course = db[courseid]
            if course["code"] == code:
                course["sections"].append(newSection)
        db.save(course)
        return True

def str2bool(v):
      return v.lower() in ("yes", "true", "t", "1")

def userNewSection():
    code = input("Course code: ")
    sectioncode = raw_input("Section codename: ")
    days = raw_input("Days (i.e. MTWRF): ")
    period = input("Period: ")
    room = raw_input("Room : ")
    double = str2bool(raw_input("Is a double period (t/f)? "))
    capacity = input("Class capacity: ")
    numRegistered = input("Number of registered students: ")
    sRegistered = []
    for i in range(0, numRegistered):
        sRegistered.append(input("studentid: "))
    teacher = raw_input("Teacher name: ")
    if newSection(code,sectioncode,days,period,room,double,capacity,numRegistered,sRegistered,teacher):
        print "section added"
        return True
    else:
        return False
#userNewSection()
