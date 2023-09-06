#movietickets

while True:
    Age=float(input("Confirm your Age:"))
    
    if Age <= 0:
        print("Please Enter a Valid Age") 
        break   
    if Age <= 3:
        Ticket_Rate=0
    elif Age <= 12:
        Ticket_Rate=15
    elif Age > 12 :
        Ticket_Rate=20   
        print("Your Ticket Price is","$",Ticket_Rate)         
    else:
        print("Please Enter your Age")      
    break
