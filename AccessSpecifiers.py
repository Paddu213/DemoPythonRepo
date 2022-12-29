#public methods--can be accessed from any where By defalt everything

class Public_Sample_AccessModifier:
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
    def display_public_sample_method(self):
        print("Course: {} - Duration: {}".format(self.course,self.duration))

#publicobj=Public_Sample_AccessModifier('Python',6)
#publicobj.display_public_sample_method()

class Protected_Sample_Class:
    _tutor=None
    _place=None
    _experience=None
    def __init__(self,tutor,place,experience):
        self.tutor=tutor
        self.place=place
        self.experience=experience
    def _displayTutorDetails(self):
        print("Tutor: {} - Place: {} - Experience: {}".format(self.tutor,self.place,self.experience))

#derivedClassObj=Protected_Sample_Class('padmavathi','markapur',1)
#derivedClassObj._displayTutorDetails()

class Derived_Protected_Class(Protected_Sample_Class):
    def tryToDisplayProtectedMethod(self):
        self._displayTutorDetails()
derivedObj=Derived_Protected_Class("paddu","mrkp",1)
derivedObj.tryToDisplayProtectedMethod()