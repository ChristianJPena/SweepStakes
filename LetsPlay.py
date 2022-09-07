print("Guess That Number between 1 & 100!")

import random
random_number = random.randint(1, 100)
does_it_match = False

guessed_number = int(input("What say you? "))
while does_it_match is False:
    if guessed_number != random_number:
        print("An incorrect guess, but there are still guesses left")
        guessed_number = int(input("What say you this time? "))

    if guessed_number != random_number:
        print("An incorrect guess, but there are still guesses left")
        guessed_number = int(input("What say you this time? "))

    if guessed_number != random_number:
        print("An incorrect guess, but there are still guesses left")
        if random_number >= 1 and random_number <=20 :
            print("HINT: 1-20")   
        elif random_number >= 21 and random_number <=40:
            print("HINT: 21-40")   
        elif random_number >= 41 and random_number <=60:
            print("HINT: 41-60")   
        elif random_number >=61 and random_number <=80:
            print("HINT: 61-80")   
        else:
            print("HINT: 81-100")   
        guessed_number = int(input("What say you this time? "))

    if guessed_number != random_number:
        print("An incorrect guess, but there are still guesses left")
        guessed_number = int(input("What say you this time? "))

    if guessed_number != random_number:
        print("An incorrect guess, there are no more guesses left")
        print(random_number)
        print("Not good at this game, huh? You have lost!")
        break
        
    else:
        print("A correct guess")
        print("Congratulations, you have won!")
        does_it_match = True




# for x in range(6):
#     print("An incorrect guess, but there are still guesses left")




# print(random_number)