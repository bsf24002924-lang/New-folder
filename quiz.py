print(" Do You want to play game:","yes/no")

playing=input("Enter your choice ")
if(playing.lower()!="yes"):
   quit()
print("Welcome to Quiz game: )")
score=0

answer=(input("what is this year? "))

if(answer.lower()=="2025"):
   print("Correct!")
   score+=1
else:
   print("Sorry, Wrong answer")

answer=(input("what is this Month? "))

if(answer.lower()=="november"):
   print("Correct!")
   score+=1
else:
   print("Sorry, Wrong answer")

print(f"Your score is {score}")

print(f"You got {score} scores")




