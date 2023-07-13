class Parent:  # Prent class or Super class

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

class Child(Parent):  #Child inheriting all features/methdos of parent class
    # child class or sub class
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")




p1 = Parent()
p1.feature1()
p1.feature2()

c1 = Child()
c1.feature3() 
c1.feature4()