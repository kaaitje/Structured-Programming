import random


def random_guess(number):
    guess = False
    while int(guess) != number:
        guess = input('What is your guess?')

        if number == int(guess):
            return 'you guessed it!!'


guess_this = random.randrange(10, 0, -1)
print(guess_this)
#print(random_guess(number)


# returnt none als jehet niet in de eerste ronde gokt??
def recursive_rand_guess(number):
    guess = input('What is your guess?')
    if int(guess) == number:
        return 'you guessed it!!'
    else:
        recursive_rand_guess(number)


print(recursive_rand_guess(guess_this))
