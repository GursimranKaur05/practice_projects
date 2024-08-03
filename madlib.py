#youtuber = "xyz" #variable to store a string

##a few ways to concatenate strings
#print("subscribe to "+youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")
'''
print("Madlib : Enter the following words to complete a passage")
adj = input("Adjective: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to  {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
'''

import random

def randomMadlib():
    num = random.randrange(1,5)
    if num == 1:
        madlib = f"The {adj} {famous_person} effortlessly {verb1} and {verb2}."
    elif num == 2:
        madlib = f"{famous_person} is {adj} and {verb1} and {verb2}."
    elif num == 3:
        madlib = f"The {adj} {famous_person} {verb1} his speech and {verb2} the audience."
    elif num == 4:
        madlib= f"According to {famous_person}, The simple excercise of {verb1} has {adj} effects and can {verb2} benefit everyone."
    else:
        madlib= f"{verb1} to help other people will make you feel {adj} and then you can {verb2} with {famous_person}."
        
    return madlib

again = 1
while again != 0:
    print("Enter the following words to complete a passage")
    adj = input("Adjective: ")
    verb1 = input("verb1: ")
    verb2 = input("verb2: ")
    famous_person = input("Famous person: ")

    print(randomMadlib())

    print("------------------")
    again = int(input("Play Again? Type 1 for yes or type 0 to exit : "))
