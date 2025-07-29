# password guessing game 

import random

easyWords=["apple","orange","tiger","plane","water","phone"]
mediumWords=["elephant","waterfall","laptop","dancing","bedroom"]
hardWords=["Belgium","Portugue","Anaconda","Benchmark"]

print("Welcome to Password Guessing Game! \n")
print("Choose difficulty level(easy,medium,hard):\n")

level=input("Enter difficulty: \n").lower()
if level=="easy":
    secret=random.choice(easyWords)
elif level=="medium":
    secret=random.choice(mediumWords)
elif level=="hard":
    secret=random.choice(hardWords)
else:
    print("Invalid choice! defaulting to easy Level:\n")
    secret=random.choice(easyWords)

attempts=0
print("Guess the secret password: ")
while True:
    guess=input("Guess word: ").lower()
    attempts +=1

    if guess==secret:
        print("Congratualtions! You guessed right password\n")
        break
    
    hint=""
    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint +=guess[i]
        else:
            hint +='_'
    print("Hint: "+hint)
print("Game Over!\n")