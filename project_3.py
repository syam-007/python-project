height= int(input("Ënter your height: "))
bill=0
if height>120:
     print("You can ride")
     age=int(input("Enter your age: "))
     if age >18:
          bill=12
          print("you can ride")
     elif age ==12:
          bill =7
          print("you can ride")
     elif age == 18:
          bill = 7
          print("you can ride")
     elif age<12:
          bill=5
          print("you can ride")
     photo=input("do u want photo? Y o N:")

     if "Y":
          bill+=3
          print(f"Your total bill {bill}")

else:
     print("Sorry u can't ride")