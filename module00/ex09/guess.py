from random import randint

print("""
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")

nb2guess = randint(1, 99)

attempt = 0
while True:
    print("What's your guess between 1 and 99?")
    entry = input()
    if entry == "exit":
        print("Goodbye!")
        break
    try:
        attempt += 1
        guess = int(entry)
    except ValueError:
        print("That's not a number.")
        continue
    if guess == nb2guess:
        if nb2guess == 42:
            print("<reference to Douglous Adans>.")
        if attempt == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print(f"Congratulations, you've got it!\nYou won in {attempt} attempts")
        break
    elif guess > nb2guess:
        print("Too high!")
    else:
        print("Too low!")
