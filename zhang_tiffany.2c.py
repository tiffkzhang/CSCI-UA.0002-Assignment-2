import random

print("I'm thinking of a number 1 and 11.\n")
number = random.randint(1,11)

guess = int(input('Guess my number: '))
if  guess == number:
    print('You got it!\n')
else:
    if guess < number:
        print('Too low, try again.\n')
    else:
        print('Too high, try again.\n')

    guess = int(input('Guess my number: '))
    if guess == number:
        print('You got it!\n')
    else:
        if guess < number:
            print('Too low, try again.\n')
        else:
            print('Too high, try again.\n')
       
        guess = int(input('Guess my number: '))
        if guess == number:
            print('You got it!\n')
        else:
            print('Sorry, game over.\n')

print('The secret number was', number)
        


    

   



