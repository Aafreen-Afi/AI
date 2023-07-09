"""
1. print 'CORRECT' if i == 10
Output:
value: 10
correct
"""
i = int(input("Value: "))
if(i == 10):
    print("Correct")

"""
2. Check the password, using if and else
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
3. Category the people by their age like children, adult, citizen, senior citizen
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
4. Find whether given number is positive or negative
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
5. Check whether the given number is divisible by 5
Output:
Enter a number to check:22
No is not divisible by 5
"""
num=int(input("Enter a number to check:"))
if((num%5)==0):
    print("No is divisible by 5")
else:
    print("No is not divisible by 5")