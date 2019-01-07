# Every class method takes 1st argument as 'self'
# Which refers to the current calling object
# 'self' is a temporary place-holder for object name
class Employee:
   'Common base class for all employees'
   empCount = 0

#access Class members (within class BUT not any method) by 'class_name.member'
#access instance members (within method of a class) by 'obj_name.member'


   #special method called class constructor or initialization method
   #python calls this automatically when you create an object of a class
   #represented as _name_(arguments)
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  "\nSalary : ", self.salary


#instantiation and calling methods

obj = Employee('Amey', '$10000')

obj.displayCount()
obj.displayEmployee()
