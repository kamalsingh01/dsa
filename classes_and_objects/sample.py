# The 'self' is a reference to the current instant/object of the class and is used to access variables that belonmgs to the class
# There can exiast millions of objects of a class.

#class definition
class Person:
    # default values, can be changed.
    name = "Kamal"
    job = "SDE"
    networth = 10
    def info(self):     # self matlab woh object jispe yeh function call ho rha h
        print(f"{self.name} is a {self.job}")

p1 = Person()
p2 = Person()
p3 = Person()
p1.name = "Shubham"
p1.networth = 30

p2.name = "Kasin"
p2.job = "HR"
p1.info()
p2.info()
p3.info()  #we didn't assign any value to variables of p3 object, so default values are gonna used.