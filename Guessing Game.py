# guessing game
print("Tallest in the land, a spotted tower,\nWith leaves as treats for many an hour.")
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Who am I?\n:")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("***Congratulation***\nYou win!")
