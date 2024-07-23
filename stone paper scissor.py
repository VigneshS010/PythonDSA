import random 

user_mark=0
com_mark=0

options=["stone","paper","scissor"]



while True:
    u_choise= input("Stone/Paper/Scissor or to quit press Q....!").lower()
    if u_choise=="q":
        print("Ok...Lets quit it..")
        break
    if u_choise not in options:
        continue

    c_num=random.randint(0,2)
    c_choise=options[c_num]
    print("Compputer Picked",c_choise)
   
    if u_choise=="stone" and  c_choise=="scissor":
        print("You Win..!")
        print("You got 1 point")
        user_mark+=1
    elif u_choise=="scissor"and c_choise=="paper":
        print("You Win..!")
        print("You got 1 point")
        user_mark+=1
    elif u_choise=="paper" and c_choise=="stone":
        print("You Win..!")
        print("You got 1 point")
        user_mark+=1
    elif u_choise==c_choise:
        print("You both picked same...no points, try again")
    else:
        print (" Computer wins...!")
        print("Computer got 1 point")
        com_mark+=1


print (" You Scored ",user_mark)
print (" Computer Scored ",com_mark)

