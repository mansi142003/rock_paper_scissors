print ("welcome to my computer quiz!")
playing = input("do you want to play?")
if playing.lower!="yes"
  quit()
print ("okay! Lets play:)")
score = 0
answer = input("what does cpu stand for?")
if answer.lower()=="central processing unit":
  print("correct!")
  score+=1
else:
  print("Incorrect!")

answer = input("what is the value of pie?")
if answer.lower()=="3.14":
  print("correct!")
  score+=1
else:
  print("Incorrect!")

 
answer = input("what is the most favorite programming language")
if answer.lower()=="python":
  print("correct!")
  score+=1
else:
  print("Incorrect!")
  print ("you got"+ str(score)+"question correct!")