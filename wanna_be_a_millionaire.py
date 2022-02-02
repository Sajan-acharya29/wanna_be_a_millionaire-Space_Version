# Who wants to be a Millionaire??

# The progression in this "short" version of millionaire should be:
# 1 answer correct: $500
# 2 answers correct: $1000
# 3 answers correct: $5000
# 4 answers correct: $20000  15000
# 5 answers correct: $50000   30000
# 6 answers correct: $250000
# 7 answers correct: $500000
# 8 answers correct: $1000000

import time
print ("Loading   ")
time.sleep(0.5)
print ("Loading.  ")
time.sleep(0.5)
print ("Loading.. ")
time.sleep(0.5)
print ("Loading...")
time.sleep(0.5)
print ("******")

name = str(input("Please enter your name? "))

print(" ")

print((("Welcome to Millionaire game!")).center(60)) # center alligning the title

print ("******".center(60))

print("Hey", str.title(name) + str("!"), "Currently you have", str("$0."))

continue_game =  1
print(" ")

#first questions
print("choose the correct choice. Pick either a, b , c or d")
while continue_game !=0 :
  print("# How many planets are in our solar system? ")
  print("a. 5    b. 7     c. 8      d.  9")
  ans_choice = str(input("choose the answer >>"))
  if ans_choice == str("c"):
    print("Correct!")
    #won_amt= won_amt + 500
    print("Currently you have made "+ str("$500")+".")
  else:
   continue_game = continue_game - 1
   print("I'm sorry, that is incorrect.")
   print("You have been able to win "+ str("0") +".")
  

  #next questionnn
  if continue_game !=0 :
    print("")
    #second question

    print("# How many natural satellites does the Earth have? ")
    print("a. 1    b. 2     c. 3      d.  None")
    ans_choice = str(input("choose the answer >>"))
    if ans_choice == str("a"):
       print("Correct!")
      # won_amt= won_amt + 4000
       print("Currently you have made "+ str("$1000")+".")
    else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$500")+".")

  else:
    print("")

  #next questionnn

  if continue_game !=0 :
     print("")
   
     print("# What's a group of stars that represent an earthly object called? ")
     print("a. A comastellation    b. A nebula   c. A galaxy       d.  A constellation")

     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("d"):
       print("Correct!")
       #won_amt= won_amt + 
       print("Currently you have made "+ str("$5000")+".")
     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$1000")+".")
  else:
    print("")

##########################################
  
  if continue_game !=0 :
     print("")
     #3rd question

     print("'#The Red Planet' is the poetic name for ... ? ")
     print("a. A Jupiter    b.  Saturn   c. Mars       d.  Venus")

     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("c"):
       print("Correct!")
       #won_amt= won_amt + 500
       print("Currently you have made "+ str("$20000")+".")
     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$5000")+".")

  else:
    print("")


  if continue_game !=0 :
     print("")
     #3rd question
     print("# Saturn is best known for its gorgeous ______. ")
     print("a. Craters    b. Sunrises    c. Mountains   d.  Rings")
     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("d"):
       print("Correct!")
       #won_amt= won_amt + 500
       print("Currently you have made "+ str("$50000")+ ".")
     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$20000")+".")

  else:
    print("")


  if continue_game !=0 :
     print("")
     #3rd question

     print("# What's a group of stars that represent an earthly object called? ")
     print("a. A comastellation    b. A nebula   c. A galaxy       d.  A constellation")
     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("d"):
       print("Correct!")
       #won_amt= won_amt + 500
       print("Currently you have made "+ str("$250000")+".")
     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$50000")+".")


  else:
    print("")



  if continue_game !=0 :
     print("")
     #3rd question

     print("# A ball of ice and dust with a long, glowing tail is called what? ")
     print("a. An asteroid    b.  A blue dwarf  c. A comet  d.  A meteor")
     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("c"):
       print("Correct!")
       #won_amt= won_amt + 500
       print("Currently you have made "+ str("$500000")+ ".")
     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$250000")+".")
  else:
    print("")


  if continue_game !=0 :
     print("")
     #3rd question

     print("# Which of these terms is used to refer to the moon? ")
     print("a. Ceser      b. Lunar      c. Saren        d. All of these")
     ans_choice = str(input("choose the answer >>"))
     if ans_choice == str("b"):
       print("Correct!")
       #won_amt= won_amt + 1000000
       print("Currently you have made "+ str("$1000000")+ ".")
       print("Congratulations!!!")
       print("You are a millionaire! ")
       continue_game = continue_game - 1

     else:
       continue_game = continue_game - 1
       print("I'm sorry, that is incorrect.")
       print("You have been able to win "+ str("$500000")+ ".")

print("Thank you for playing")

