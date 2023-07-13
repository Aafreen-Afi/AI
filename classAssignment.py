class classAssignment():
    def Subfields():
        subfileds = ["Machine Learning","Neural Network","Vision","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are :")
        for fields in subfileds:
            print(fields)
            sub = fields
        return sub
    
    def OddEven():
        num=int(input("Enter a number :"))
        if((num%2)==0):
            print(num,"is Even number")
            message = "Even number"
        else:
            print(num,"is Odd number")
            message = "Odd number"
        return message
    
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
    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total = sub1+sub2+sub3+sub4+sub5
        Percentage = Total/5
        print("Total : ",Total)
        print("Percentage : ",Percentage)
        return Percentage
    
    def triangle():
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
    