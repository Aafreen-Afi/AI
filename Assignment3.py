"""
1. print 0 to 20 by using range
Output:
0 to 19 one by one vertical
"""
for num in range(0,20):
    print(num)

"""
2. Print range 10 to 20
Output:
10 11 12 13 14 15 16 17 18 19
"""
for num in range(10,20):
    print(num, end=" ")

"""
3. Print number of items in the list by using 'len'
Output:
[10, 20, 14, 55, 43, 87, 76]
Number of item in the List2:
7
"""
List=[10, 20, 14, 55, 43, 87, 76]
print(List)
Len= len(List)
print("Number of item in the List2:\n",Len)

"""
4. print 
Output: 
Aritifical Intelligence
A to e one by one vertical
"""
Str="Artificial Intelligence"
for i in Str:
    print(i)

"""
5. print this mixered datatype using Tuples
Output:
(1, 'Welcome', 2, 'Hope')
"""
tuples1=(1, 'Welcome', 2, 'Hope')
print(tuples1)

"""
6. Output:
((0, 1, 2, 3), ('python', 'HOPE'))
"""
tuples1 = (0,1,2,3)
tuples2 = ('pyhton','HOPE')
tuples3 = (tuples1, tuples2)
print(tuples3)

"""
7. Print Odd NUmbers in the list
Output:
(20,10,16,19,25,1,276,188)
19 is odd
25 is odd
1 is odd
"""
list1 = (20,10,16,19,25,1,276,188)
print(list1)
for num in list1:
    if((num%2)==1):
        print(num,"is odd")

"""
8. Print Even number in the list
Output:
(20,10,16,19,25,1,276,188)
20 is even
10 is even
16 is even
276 is even
188 is even
"""
list1 = (20,10,16,19,25,1,276,188)
print(list1)
for num in list1:
    if((num%2)==0):
        print(num,"is even")

"""
9. print 'CORRECT' if i == 10
Output:
value: 10
correct
"""
i = int(input("Value: "))
if(i == 10):
    print("Correct")

"""
10. Check the password, using if and else
Output:
Enter the password: HOPE@123
Your password is correct
"""
password= input("Enter the password: ")
if(password == "HOPE@123"):
    print("Your password is correct")
else:
    print("Your password is wrong")

"""
11. Catagory the people by their age like children, adult, citizen, senior citizen
Output:
age: 20
Adult
"""
age=int(input("Enter the age : "))
if(age<18):
   print("Children")
elif(age<35):
   print("Adult")
elif(age<59):
   print("Citizen")
else:
   print("Senior Citizen")

"""
12. Find whether given number is positive or negative
Output:
Enter any number:1
No is positive
"""
num = float(input("Enter any number:"))
if(num > 0):
    print("No is positive")
elif(num == 0):
    print("No is zero")
else:
    print("No is negative")

"""
13. Check whether the given number is divisible by 5
Output:
Enter a number to check:22
No is not divisible by 5
"""
num=int(input("Enter a number to check:"))
if((num%5)==0):
    print("No is divisible by 5")
else:
    print("No is not divisible by 5")