print("Welcome to Python pizza Deliveries!")


height=int(input("Enter your height:"))
if height >=120:
    age=int(input("Enter your age:"))
    bill=0
    if age>18:
        print("You have to pay:$12")
        bill+=12
    elif age<12:
        print("you ahve to pay:$5")
        bill+=5
    elif age<=18:
        print("you have to pay:$7")
        bill+=7
photo=input("Do u want photo?y or N?")
if "Y":
    bill+=3
print(f"your total bill {bill}")


