# 1. Output ==> Welcome to Assignment-1
print("Welcome to Assignment-1")

"""2. Output
Num1= 10
Num2= 30
Add= 40
"""
Num1=int(input("Num1= "))
Num2=int(input("Num2= "))
Add=Num1+Num2
print("Add= ",Add)


""" Body Mass Index
3. Output
Enter the BMI Index:34
Very Overweight
"""
BMI=float(input("Enter the BMI Index:"))
if(BMI<18.5):
	print("Underweight")
elif(BMI<24.9):
	print("Normal Range")
elif(BMI<29.9):
	print("Over Weight")
else:
	print("Very Overweight")