from random import randint

guesses = 0;
number = randint(0,30)
print("You will get 5 attempts to guess a number between 0 to 30")

while guesses < 5:
    print("Take a guess.")
    guess = input()
    guesses = guesses + 1
    if guess < number:
	    print("Your guess is too low")
		
    if guess > number:
		print("Your guess is too high")
	
    if guess == number:
		number1 = str(number)
		guesses1 = str(guesses)
		print("You guessed the right number, i.e " + number1 + " in " + guesses1 + " attempts.")
		break
	
if guess != number:
	number = str(number)
	print("You have used all your attempts, the correct number was " + number)
