class Base1:
    def display(self):
        print("Parent1")
class Base2:
    def display1(self):
        print("Parent2")
class Derived(Base1,Base2):
    def display(self):
        print("child1")
    def display1(self):
        print("child2")
ob=Derived()
ob.display()
ob.display1()