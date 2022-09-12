# /////////////////////////////////////////225
# class MyClass:
#     x=10
# obj=MyClass()
# print(f"Value of class's attribute X is: {obj.x}")

# //////////////////////////////////////////////226
# class MyClass:
#     def func(self):
#         print("Hello, I'm a Class's function")

# obj=MyClass()
# obj.func()

        
# ///////////////////////////////////////////227
# class MyClass:
#     def __init__(self):
#         print("Hello from init() function[constructor]")
#     def func(self):
#         print("Hello from func() function")

# obj=MyClass()
# obj.func()
        
# ////////////////////////////////////////228
# class VotingAge:
#     def __init__(self,eligibleAge):
#         self.eligibleAge=eligibleAge

#     def isEligible(self,user_age):
#         if user_age>=self.eligibleAge:
#             print('Your are Eligible for Voting')
#         else:
#             print("Your are Not Eligible for Voting")

# v1= VotingAge(18)
# v1.isEligible(25)

# v2= VotingAge(16)
# v2.isEligible(14)

# ////////////////////////////////////////////229
# class Student:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course
#     def show(self):
#         print("Student Details:")
#         print("Name:",b.name)
#         print("Course:",b.course)
# b = Student("Anmol","B.tech")
# b.show()
# b.name="Mohit"
# b.course="Bsc"
# print("\nAfter Modifying Details")
# b.show()

# ///////////////////////////////////////////230
# class Student:
#     def __init__(self,name,course,sex):
#         self.name=name
#         self.course=course
#         self.sex=sex
# s = Student("Anmol","B.Tech","Male")

# print("Student Details:")
# print("Name:",s.name)
# print("course",s.course)
# print("sex",s.sex)

# # deleting sex

# del s.sex

# print("\nStudent Details:")
# print("Name:",s.name)
# print("course",s.course)
# # print("sex",s.sex)>>error

# ////////////////////////////////////231
# class Student:
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course

#     def show(self):
#         print("\nStudent deteles")
#         print("Name :",self.name)
#         print("course:",self.course)
# s1=Student("anmol","b.tech")
# s2=Student("mohit","bsc")

# s1.show()
# s2.show()

# del s2
# s1.show()
# s2.show()>>error
# /////////////////////////////////////232
# class MyClass:
#     pass

# //////////////////////////////////////////
