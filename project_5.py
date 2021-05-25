print("Welcome to the Love calculator:")
name1=input("What your name: \n")
name2=input("What is there name:\n ")

name = (name1 + name2).lower()
cnt=0
name_t=name.count("t")
cnt+=name_t
name_r=name.count("r")
cnt+=name_r
name_u=name.count("u")
cnt+=name_u
name_e=name.count("e")
cnt+=name_e
a = cnt

cnt2=0
name_t=name.count("l")
cnt2+=name_t
name_r=name.count("o")
cnt2+=name_r
name_u=name.count("v")
cnt2+=name_u
name_e=name.count("e")
cnt2+=name_e
b = cnt2
c =int(str(a)+str(b))
print(c)

if (c)<=47:
    print(f"Your score is {c},you are alright together.")
elif (c)>=100:
     print(f"Your score is {c},you go together like coke and mentos.")
elif c>=54 and c<100:
    print(f"Your score is {c}")

