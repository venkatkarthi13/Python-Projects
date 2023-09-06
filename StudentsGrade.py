
 #Marks

def subjects(English,Maths,Science,Social,Computer):
    average=(English+Maths+Science+Social+Computer)
    Grade=average//5
      
    if Grade>=50:
        return "You've got pass mark with C Grade"
    elif Grade>=70:
        return "You've got pass mark with B Grade"
    elif Grade>=90:
        return "You've got pass mark with A Grade"
    elif Grade>100:
        return "Please Enter Correct Value"
    else:
        return "You got Failed :( Better Luck Next Time!"
    
English=float(input("Enter your English mark:"))
Maths=float(input("Enter your Maths mark:"))
Science=float(input("Enter your Science mark:"))
Social=float(input("Enter your Social mark:"))
Computer=float(input("Enter your Computer mark:"))

if English > 100 or Maths > 100 or Science > 100 or Social > 100 or Computer > 100:
    print("Please Enter Correct value(0-100)")
    
else:
    Result=subjects(English,Maths,Science,Social,Computer)
    print("Your final grade:", Result)

#i'm used // as a floor property for rounding the value 
    average=(English+Maths+Science+Social+Computer)//5
    print("your marks:",average)


