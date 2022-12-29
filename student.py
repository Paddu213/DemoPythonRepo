class Student:
    marks_bonus=1.5

    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
        self.somevalue = ""

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def something(self,middle):
        self.somevalue=self.email+self.fullname+ middle


