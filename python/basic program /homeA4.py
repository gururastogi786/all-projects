count=0
n=int(input("Please Enter The Number:- "))
for i in range(1,n+1):
    if n%i==0:
     count+=1
if count==2:
    print("your number is prime")
else:
    print("your number is not prime")    