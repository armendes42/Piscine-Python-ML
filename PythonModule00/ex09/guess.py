import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()

attempts = 0
magic_number = random.randint(1, 99)
is_forty_two = magic_number == 42

while True:
    user_input = input("What's your guess between 1 and 99?\n")
    attempts += 1
    if user_input == "exit":
        print("Goodbye!")
        break
    elif not user_input.isdigit():
        print("That's not a number.")
        continue
    number = int(user_input)
    if number < 1 or number > 99:
        print("You have to enter a number between 1 and 99!")
        continue
    elif number < magic_number:
        print("Too low!")
    elif number > magic_number:
        print("Too high!")
    elif number == magic_number:
        if is_forty_two:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if attempts == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in " + str(attempts) + " attempts!")
        break
