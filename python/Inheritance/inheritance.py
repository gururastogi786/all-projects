# //////////////////////////// SINGLE INHERITANCE 233 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Base:
#     def add(self,a,b):
#         return a+b
# class DerivedA(Base):
#     def mul(self,a,b):
#         return a*b
# n1=int(input("Enter the 1st value:- "))
# n2=int(input("Enter the 2nd value:- "))
# d=DerivedA()
# print(f"(From Base class) Addition is: {d.add(n1,n2)}")
# print(f"(From Derived class) Multiplication is: {d.mul(n1,n2)}")

# ////////////////////////////// HIERARCHICAL INHERITANCE 234 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Base:
#     a= 10
#     b= 20
# class DerivedA(Base):
#     def sum(self):
#         add=self.a+self.b
#         print("Addition is:",add)
# class DerivedB(Base):
#     def mul(self):
#         mul=self.a*self.b
#         print("Mul is:",mul)
# CA=DerivedA()
# dB=DerivedB()
# CA.sum()
# dB.mul()

# " //////////////////////////////// MULTIPLE INHERITANCE 235 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
# class cementDealer:
#     def getcementcost(self,quantity):
#         return quantity * 300
# class ironDealer:
#     def getironcost(self,quantity):
#         return quantity * 4500
# class Builder(cementDealer,ironDealer):
#     def gettotalcost(self,cq,iq):
#         c_cost=self.getcementcost(cq)
#         i_cost=self.getironcost(iq)
#         total_cost =c_cost+i_cost
#         return total_cost
# cement=int(input("Enter the Cement quantity:"))
# iron=int(input("Enter the iron quantity: "))
# b=Builder()
# total_cost=b.gettotalcost(cement,iron)
# print(f"Cement cost iron cost  TOTAL COST is : {total_cost}")

# ////////////////////////////////////// MULTILEVEL INHERITENCE 236\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class University:
#     def getUdetails(self):
#         self.uName=input("Enter University Name: ")
#         self.uRID=input("Enter Reg. (University) No.:")
#     def showUdetails(self):
#         print(f"University Name: {self.uName}")
#         print(f"University Reg. No.: {self.uRID}")


# class College(University):
#     def getClgDetails(self):
#         self.cName=input("Enter College Name:")
#         self.cRID=input("Enter Reg. (College)No.:")
#         self.getUdetails()    
#     def showClgDetails(self):
#         print("College Name:",self.cName)
#         print("College Reg. No.:",self.cRID)
#         self.showUdetails()


# class Student(College):
#     def getStudDetails(self):
#         self.uName=input("Enter Student Name: ")
#         self.sRoll=input("Enter Student's Enroll No.:")
#         self.sBranch=input("Enter Student's Branch: ")
#         self.getClgDetails()
#     def showStudDetails(self):
#         print("\nSTUDENT DETAILS:")
#         print("Student Name:",self.uName)
#         print("Student Enroll. No.:",self.sRoll)
#         print("Student Branch:",self.sBranch)
#         self.showClgDetails()

# s=Student()
# s.getStudDetails()
# s.showStudDetails()

# //////////////////////////// HYBRID INHRITANCE 237\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Student:
#     def getStudentDetails(self):
#         self.sName=input("Enter the Student Name: ")
#         self.sRoll=int(input("Enter Student's Enroll no.:"))

#     def showStudDetails(self):
#         print("\nSTUDENT DETAILS")
#         print(f"Student Name: {self.sName}")
#         print(f"Student Enroll no: {self.sRoll}")


# class Academics(Student):
#     total=0
#     def getMarks(self):
#         for i in range(5):
#             print(f"Enter Marks for Subject {(i+1)}:",end="")
#             self.marks=int(input())
#             self.total=self.total+self.marks

#     def getATotal(self):
#         self.showStudDetails()
#         return self.total


# class sports(Academics):
#     spName=""
#     grad=0

#     def getSport(self):
#         self.spName=input("Enter Sport Name:")
#         self.grad=int(input("Enter Sport Marks:"))

#     def getSmarks(self):
#         return self.grad

#     def showSport(self):
#         print("Sport Name:",self.spName)
        

# class Result(sports,Academics):
#     def getResult(self):
#         self.getStudentDetails()
#         self.getMarks()
#         self.getSport()
    

#     def showResult(self):
#         aTotal=int(self.getATotal())
#         sTotal=int(self.getSmarks())

#         per=(aTotal+sTotal)/6
#         print(f"Percentage: {per}")
#         self.showSport()

# r=Result()
# r.getResult()
# r.showResult()

# //////////////////////////// SUPER KEYWORDS 238\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# class Parent:
#     def func1(self):
#         print("This is Parant Function1.")

# class Child(Parent):
#     def func1(self):
#         print("this is child function1.")

#     def func2(self):
#         super().func1()
#         self.func1()
#         print("This is Child function2")

# ch=Child()
# ch.func2()
