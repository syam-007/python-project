print("Welcome to Python pizza Deliverise!")


size=input("What size pizza do you want? S,M or L:")
add_pepperoni= input("Do you want pepperoni? Y or N")
extra_chesses= input("Do you want chesses? Y or N:")
bill=0
if size=="S":
     bill+=15
elif size=="M":
     bill+=20
elif size=="L":
     bill+=25
if add_pepperoni=='Y':
     if size=="S":
          bill+=2
     elif size=="M":
          bill+=3
     elif size=="L":
          bill+=3
if extra_chesses=="Y":
     bill+=1

print(f"Your final bill {bill}")


