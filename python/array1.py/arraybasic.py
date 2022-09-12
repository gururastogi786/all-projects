# ///////////////////////////////////////////////192
# import array
# from operator import le
# arrint=array.array("i",[1,2,3,4,5])

# arrflot=array.array("f",[1.1,2.2,3.3,4.4])

# arrchar=array.array("u",["A","B","C","D"])

# print("Integer array:")
# for i in range(len(arrint)):
#     print(arrint[i])

# print("Float array\n")
# for i in range(len(arrflot)):
#     print(arrflot[i])

# print("Char array\n")
# for i in range(len(arrchar)):
#     print(arrchar[i])

# ///////////////////////////////////////////////193
# import array as arr
# arrint=arr.array("i",[1,2,3,4,5,6])
# print(f"My array\n{arrint}")
# print(f"array item index 2 is: {arrint[2]}")
# print(f"For nagetiv indexing -2 is: {arrint[-2]}")

# ///////////////////////////////////////////////////194
# import array as arr
# arrint=arr.array("i",[1,2,3,4,5,6,7,8,9,10,11])
# print(f"My array\n{arrint}")
# print(f"array [2:5]: {arrint[2:5]}")
# print(f"array [1::2]: {arrint[1::2]}")
# print(f"array [-10:-1:2]: {arrint[-10:-1:2]}")
# print(f"array [2::2]: {arrint[2::2]}")

# ///////////////////////////////////////////////////195
# import array as arr
# arrint=arr.array("i",[10,20,100,40,50,60,70,80,90])
# print(f"My array:- {arrint}")
# arrint[2]=30
# print(f"After modifying item [2]:{arrint}\n")
# arrint[2:7]=arr.array("i",[-30,-40,-50,-60,-70])
# print(f"Modify [2:7]: [-30,-40,-50,-60,-70]:\n{arrint} ")

# ////////////////////////////////////////////////////196
# import array as arr
# arrint=arr.array("i",[10,20,100,40,50,60,70,80,90])
# print(f"My array: {arrint}")
# arrint.append(100)
# print(f"After apending: {arrint}")

# ////////////////////////////////////////////197
# import array as arr
# arrint=arr.array("i",[10,20,100,40,50,60,70,80,90])
# print(f"My array: {arrint}")
# arrint.insert(2,30)
# print(f"after inserting: {arrint}")

# //////////////////////////////////////////////////198
# import array as arr
# arrint=arr.array("i",[10, 20, 30, 100, 40, 50, 60, 70, 80, 90])
# print(f"My array: {arrint}")
# del arrint[3]
# print(f"after deleting [3]: {arrint}")

# ////////////////////////////////////////////////199
# import array as arr
# arrint=arr.array("i",[10,20,30,40,100,50,60,70,80,90])
# print(f"My list: {arrint}")
# arrint.remove(100)
# print(f"After removing 100 : {arrint}")

# ////////////////////////////////////////////////////200
# import array as arr
# arrint=arr.array("i",[10,20,30,40,50,60,70,80])
# print(f"My array: {arrint}")
# arrint.pop(3)
# print(f"After poping 3 {arrint}")

# ///////////////////////////////////////////////////////201
# import array as arr
# arrint=arr.array("i",[10,20,30,40,50,60,70,80,90])
# print(f"\nMy Array: {arrint}")
# arrint.reverse()
# print(f"After revers item: {arrint}")

# ///////////////////////////////////////////////////////202
# import array as arr
# arrint=arr.array("i",[10,20,30,40,50,60,70,80,90])
# print(f"\nMy Array:\n {arrint}")
# arrint=arrint[::-1]
# print(f"\nAfter revers (using indexing): \n{arrint}")

# ///////////////////////////////////////////////////////203
# import array as arr
# numa=arr.array("i",[10,20,30,40,50])
# numb=arr.array("i",[60,70,80,90,100])
# print(f"My array:\n {numa}")
# numa.extend(numb)
# print(f"\nAfter extend array: {numa}")

# ///////////////////////////////////////////////////////204
# import array as arr
# numA=arr.array("i",[10,20,30,40,50])
# numB=arr.array("i",[60,70,80,90,100])
# numC=numA+numB
# print("Array A",numA)
# print("Array B",numB)
# print("Array C",numC)

# ///////////////////////////////////////////////////////205
# import array as arr
# numA=arr.array("i",[1,2,5,86,6,58,6,8,6,4,2,36,5,6,55,5])
# print(f"My array:\n{numA}")
# numA=numA.count(5)
# print(f"Count number 5 in array:- {numA}")
