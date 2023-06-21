# Constructor in Python

'''
    > Constructor mainly initializes the class variables.
    > __init__() is a dunder method which is used to define constructor for the class which inturn initailizes the class valribales(data membrs) of the class.
    > everytime an instance is created, constructor (__init__()) is called.
    > Whenever we define an instance of the class and pass the arguments, those values are passed to constructer and stored in class varibales for that instance.
    > class instance is passed automatically as self to the constructor, we need not to pass it at instance creation
    > Default Constructor : when any constructor accepts any arguments from object and contains only self as argument
'''

class Person:
    # name = "Kamal"
    # job = "SDE"

    #defining constructor(parameterized Constructor)
    def __init__(self, n ,j):     #here we are overrding the __init__() method
        print("Hey I am a person")
        self.name = n
        self.job = j

    #for most of the methods defining in a class, it is must to pass self as argument 
    def info(self):
        print(f"{self.name} is a {self.job}")


p1 = Person("Kamal", "SRE") #constrcutor is called.
p1.info()

p2 = Person("Divya", "HR")
p2.info()
