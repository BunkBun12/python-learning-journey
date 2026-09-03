import random

words = ["apple", "banana", "mango"]

print("WORDLE")

word_picker = random.choice(words)
word_length = len(word_picker)

print(f"The word is {word_length} letters long")

for i in range(word_length):
    print("_", end=" ")

print()

chances = 3

while chances > 0:

    choice = input(
        f"Do you want to play the {word_length} letter word? "
        "y (yes) or n (no): "
        ).lower()

    if choice == "n":
        print("Game ended.")
        break

    elif choice == "y":

        print(f"You have {chances} chances to guess the word.")

        guess = input("Enter the word: ").lower()

        if len(guess) != word_length:
            print(f"Your word must have {word_length} letters!")
            continue

        if guess == word_picker:
            print("🎉 You got it!")
            break

        else:
            chances -= 1

            for i in range(word_length):

                if guess[i] == word_picker[i]:
                    print(f"{guess[i]} 🟩 is in the correct position")

                elif guess[i] in word_picker:
                    print(f"{guess[i]} 🟨 exists but is in the wrong position")

                else:
                    print(f"{guess[i]} ⬜ does not exist in the word")

            print(f"You have {chances} chances left.")

    else:
        print("Please enter y or n.")

if chances == 0:
    print(f"\nYou lost! The word was: {word_picker}")