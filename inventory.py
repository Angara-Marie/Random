provisions = {"pads":100, "lotion":100, "bar_soap":100, "deodrant":100, "omo":0}
student_received = ["Tessa"]

supply = input("What supply was given? ")
student = input("Which student received? ")

# def supplies():
#     print("Enter 1: To add to provisions")
#     print("Enter 2: To check provisions")
#     print("Enter Q: To QUIT")
#     return input("What would you like to do?")

# run = supplies()

# while True:
#     if run == 1:

if supply in provisions:
    if student in student_received:
        print(f"{student} has received their provisions")
    else:
        if provisions[supply] > 0:
            provisions[supply]-= 1
            print(provisions)
            student_received.append(student) 
            print(student_received)  
            print(f"{student} has recieved {supply}") 
        elif provisions[supply] <= 0:
            print(f"{supply} out of stock")  
        else:
            print(f"{student} has not received provisions because we are out of {supply}")    
else:
    print(f"{supply} are out of stock")            