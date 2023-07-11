""" 
1. Subfields()
Sub-fields in AI are:
Machine Learning
Neural Network
Vision
Speech Processing
Natural Language Processing
"""
subfileds = ["Machine Learning","Neural Network","Vision","Speech Processing","Natural Language Processing"]
def Subfields():
    print("Sub-fields in AI are :")
    for fields in subfileds:
        print(fields)
        sub = fields
    return sub
Subfields()

"""
2. OddEven()
Enter a number: 4
4 is Even number
"""
def OddEven():
    num=int(input("Enter a number :"))
    if((num%2)==0):
        print(num,"is Even number")
        message = "Even number"
    else:
        print(num,"is Odd number")
        message = "Odd number"
    return message
OddEven()

"""
3. Elegible()
Your Gender :Male
Your Age:18
NOT ELIGIBLE
"""
def Eligible():
    gender=input("Your Gender :")
    age=int(input("Your Age :"))
    if(gender=="Male" and age>=21):
        print("ELIGIBLE")
        eligible = "ELIGIBLE"
    elif(gender=="Male" and age<21):
        print("NOT ELIGIBLE")
        eligible = "NOT ELIGIBLE"
    elif(gender=="Female" and age>=18):
        print("ELIGIBLE")
        eligible = "ELIGIBLE"
    else:
        print("NOT ELIGIBLE")
        eligible = "NOT ELIGIBLE"
    return eligible
Eligible()
    
"""
4. Percentage()
Subject1=23
Subject2=45
Subject3=34
Subject4=23
Subject5=23
Total : 148
Percentage : 29.599999999998
"""
def Percentage():
    sub1=int(input("Subject1="))
    sub2=int(input("Subject2="))
    sub3=int(input("Subject3="))
    sub4=int(input("Subject4="))
    sub5=int(input("Subject5="))
    Total = sub1+sub2+sub3+sub4+sub5
    Percentage = Total/5
    print("Total : ",Total)
    print("Percentage : ",Percentage)
    return Total,Percentage
Percentage()

"""
5. Trinangle()
Height:3
Breadth:4
Area formula: (Height*Breadth)/2
Area of Triangle : 6.0
Height1:3
Height2:4
Breadth:45
Perimeter formula : Heigth1+Height2+Breadth
Perimeter of Triangle: 52
"""
def Triangle():
    Height=float(input("Height:"))
    Breadth=float(input("Breadth:"))
    Area_of_Triangle = (Height*Breadth)/2
    print("Area_of_Triangle = (Height*Breadth)/2")
    print("Area of Triangle: ",Area_of_Triangle)
    height1=int(input("Height1:"))
    height2=int(input("Height2:"))
    breadth=int(input("Breadth:"))
    Perimeter_of_Triangle = height1+height2+breadth
    print("Perimeter_of_Triangle = height1+height2+breadth")
    print("Perimeter of Triangle: ",Perimeter_of_Triangle)
    return Area_of_Triangle,Perimeter_of_Triangle
Triangle()