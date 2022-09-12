#//////////////////////////////////////ans:1
# l=["x",20,"y",10,"z",30]
# cnt=0
# st=""
# inc=0
# for c in range(1,6,2):
#     cnt=cnt+c
#     st=st+l[c-1]+"@"
#     inc=inc+l[c]
#     print(cnt,inc,st)
# /////////////////////////////////////////ans:2

# global x
# x=5
# def fun2():
#     x=3
#     print(x)
# x=x+1
# print(x)

# /////////////////////////////////////////ans:3

# str="pythonforbeginners is easytolearn"
# str2="easy"
# print("the first occurrence of str2 is at :",end="")
# print(str.find(str2))

# ////////////////////////////////////////  ans:4

# list1=[0.5*x for x in range(0,4)]
# print(list1)

# ////////////////////////// ans:5

# l1=[500,800,600,200,900]
# start=1
# sum=0
# for c in range(start,4):
#     sum=sum+l1[c]
#     print(c,":",sum)
#     sum=sum+l1[0]*10
#     print(sum)

# //////////////////////////ans:6


# x=50
# def func():
#     global x
#     print('x is',x)
#     x=2
#     print('changed global x to',x)
# func()
# print('valie of x is ',x)

# //////////////////////////// ans:7

# txt=["20","50","30","40"]
# cnt=3
# total=0
# for c in [7,5,4,6]:
#     t=txt[cnt]
#     total=float(t)+c
#     print(total)
#     cnt-=1

# //////////////// ans:8
# def ChangeList():
#     l=[]
#     l1=[]
#     l2=[]
#     for i in range(1,10):
#         l.append(i)
#     for i in range(10,1,-2):
#         l1.append(i)
#     for i in range(len(l1)):
#         l2.append(l1[i]+l[i])
#     l2.append(len(l)-len(l1))
#     print(l2)
# ChangeList()

# //////////////////////////// anms:9

# l1=[100,900,300,400,500]
# start=1
# sum=0
# for c in range(start,4):
#     sum=sum+l1[c]
#     print(c,":",sum)
#     sum=sum+l1[0]*10
#     print(sum)

# ///////////////////////////////ans:10

# def fun(s):
#     n=len(s)
#     m=""
#     for i in range(0,n):
#         if (s[i]>='a' and s[i]<='m'):
#             m=m+s[i].upper()
#         elif()


























# /////////////////////////////
# def update(a,b=5):
#     a=a//b
#     b=a%b
#     print(a,'$',b)
#     return a+b

# a = 100
# b = 30
# a = update(a,b)           
# print(a,'#',b)
# b=update(b)
# print(a,'#',b)
# a=update(a)
# print(a,'$',b)

# a = [10,11,12,13,14,15,16,17,18,19,20]
# even = []
# odd = []
# for i in a:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even,'/n',odd)
