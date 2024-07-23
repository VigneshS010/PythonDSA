print ( " Lets start a Quix\z...")
score = 0

permission= input( " Do u ready to play :")
if permission.lower() !="yes":
    print (" ok we quit this ...")
    quit()
else:
    print ( " Lets start to play")

qn1= input( "CPU stands for :")
if qn1.lower()== "central processing unit":
    print (  " your ans is correct")
    score+=1
else :
    print (" sorry bro ans is  wrong ")

qn2= input( "GPU stands for :")
if qn2.lower()== "graphical processing unit":
    print (  " your ans is correct")
    score +=1
else :
    print (" sorry bro ans is  wrong ")

print (" You sored "  , score)
print ( " Your persentage is ", (score/2) *100  ,"%")