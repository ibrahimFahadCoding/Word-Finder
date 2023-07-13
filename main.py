import random
import time

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

let = set()
words = set() 
score = 0

enter = input("Welcome to Wordsmith! Press Enter to play!") 
time.sleep(1)
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Go!")

while len(let) != 7:
  letter = random.randint(ord('a'), ord('z'))  
  chrL = chr(letter)
  let.add(chrL)
print(let)  

while True:
  trueFail = True
  wordInput = input("Enter a word: ") 
  for item in wordInput:
    if item not in let:
      trueFail = False
  if trueFail == True:
    if wordInput not in validWords:
      print("Invalid!")
      break 
    elif wordInput in words:
      print("You already typed this word.") 
    else:
      print("Valid!")
      score += 5 
      print("Score: " + str(score))
      words.add(wordInput)
        
    
  else:
    print("Invalid!") 
    break 
        
    




  



