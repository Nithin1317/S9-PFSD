class Base:
    def add(self,a,b):
        sum=a+b
        return sum
class Derived(Base):
    def add(self,b,c):
        sub=b-c
        return sub
ob=Derived()
print(ob.add(4,1))