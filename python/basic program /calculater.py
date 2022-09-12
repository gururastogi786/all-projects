from operator import truediv
print("      WELCOME TO MY CALCULATER       ")
while(1):
    num=input("Press any key except N/(n)")
    if (num=="n"):
        print("Program end. Thanku...")
        break
    else:
        a=int(input("enter your 1st value:-"))
        b=int(input("enter your 2nd value:-"))
        print("(1) +")
        print("(2) *")
        print("(3) /")
        print("(4) -")
        x=int(input("Enter your choice:-"))
        if x==1:
            print(f"your {a} and {b} number is:-",a+b)
        elif x==2:
            print(f"your {a} and {b} number is:-",a*b)
        elif x==3:
            print(f"your {a} and {b} number is:-",a/b)
        elif x==4:
            print(f"your {a} and {b} number is:-",a-b)
    
    
   


        
    



