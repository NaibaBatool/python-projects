# fake headline generator

import random 

CelebList=["Syra khan","Kinza Saleem","Jamshed Arsalan","Shahzad Roy","Imad Wasim","Minal Khan","Raniya Shahzad"]
ActionList=["launches","cancel party","eats","dances","delares war on","angry","enjoying vacation at"]
PlacesList=["at Red Fort","At Disney Land","Bechtree Restaurant","in Lahore local train","Parliamentry court","a box of apple"]

while True:
    Celeb=random.choice(CelebList)
    action=random.choice(ActionList)
    place=random.choice(PlacesList)

    headline=f" BREAKING NEWS: {Celeb} {action} {place}"
    print("\n" + headline)

    userInput=input("\nDo you want another headline? (yes/no)").strip().lower()
    if userInput == "no":
        break

print("\n Thanks for using Fake News Headlines\n")