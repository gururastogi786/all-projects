import numbers


a=[]
num=int(input("How mani Numbers:- "))
for i in range(num):
    numbers=int(input("enter your number:-"))
    a.append(numbers)
print(f"your maximum number is:- {max(a)}")
print(f"your minimum number is:- {min(a)}")
