from time import *
import random 
def mistake(ptest,itest):
    error=0
    try:
        for i in range(len(ptest)):
            if ptest[i]!=itest[i]:
                error+=1
    except:
        error+=1
    return error




    

tests=["Typing efficiently requires more than just speed. Its about finding a balance between accuracy and momentum",
      "A consistent typing practice can help improve both speed and accuracy.",
      "Every proficient typist understands the importance of maintaining good posture while typing.",
      "The evolution of typing has been remarkable, from the mechanical typewriters of the past"]
test=random.choice(tests)
string="***********Typing Test**********\n"
cst=string.center(65)
print("\n",cst)
print(test,"\n\n")
t11=time()
testinput=input("Start here : ")
t22=time()
print(mistake(test,testinput))