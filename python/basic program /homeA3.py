def fact(n):
    if n<=1:
        return 1
    else :
        n=n*fact(n-1)
        return n
n=int(input("Please Enter the Number:- "))
print(f"Factorial Of:{n} Is:- {fact(n)}")