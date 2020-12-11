#create a class student of attributes roll number, name, course, total
#must have methods for setting & printing these attributes


class student:
    def set_student(self,roll,name,course,total):
       #instance variables , to call instance varibale we have to use "self" keyword
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total

    def print_student(self):
        print("roll",self.roll)
        print("name",self.name)
        print("course",self.course)
        print("total",self.total)
#references
obj=student()
obj.set_student(1001,"ajay","cse",586)
obj.print_student() #output
# roll 1001
# name ajay
# course cse
# total 586

#we can access instance variable outside class using the references
print(obj.name) #output
#ajay