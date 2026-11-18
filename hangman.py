
import random

def display_word(secret_word, guessed_letters):
    """Display correctly guessed letters and hide remaining letters."""
    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display

def play_game():


    words = ["python", "computer", "college", "program", "coding"]


    secret_word = random.choice(words)


    guessed_letters = set()


    max_attempts = 6
    attempts = 0

    print("\n================================")
    print("        HANGMAN GAME")
    print("================================")
    print("Guess the hidden word!")
    print("You can make maximum 6 incorrect guesses.")


    while attempts < max_attempts:

        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses:", attempts)
        print("Remaining attempts:", max_attempts - attempts)


        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The correct word was:", secret_word)
            return


        guess = input("Enter one letter: ").lower().strip()


        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter only one alphabet.")
            continue


        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue


        guessed_letters.add(guess)


        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts += 1
            print("Wrong guess!")


    print("\nGAME OVER!")
    print("You have used all 6 incorrect guesses.")
    print("The correct word was:", secret_word)


def main():

    while True:
        play_game()

        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if choice != "yes":
            print("\nThank you for playing Hangman!")
            break


if __name__ == "__main__":
    main()