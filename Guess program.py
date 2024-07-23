import random

top_range = input( " Type the range of the number :")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range< 0:
        print ( "Enter values larger than  0 only")
else:
    print ("Enter the numbers only, try again")
    quit()

random_num = random.randint(0,top_range)
print (random_num)

mark=0
while True:
    mark+=1
    guess=input("Enter your guess :")
    if guess.isdigit():
         guess=int(guess)
         if guess<0:
             print("THe value must be greater than 0")
    else:
        print(" Enter the numbers only...")


    if guess==random_num:
        print(" Your ans is correct....!")
        break
    elif guess<random_num:
        print (" You r below the num")
    else:
        print(" You are above the num")
    

print ( "You guesses",mark,"times...")
print("and your average of the guess is",((guess/top_range)*100)  )


