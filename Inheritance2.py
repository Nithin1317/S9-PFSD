class Base:
    def display(self):
        print("GrandParent")
class Derived1(Base):
    def display(self):
        print("Parent")
class Derived2(Derived1):
    def display(self):
        print("Child")
ob=Derived2()
ob.display()