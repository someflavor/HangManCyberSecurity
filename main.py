import random

def hangman():
    # Word list with cybersecurity-related terms and hints
    words_with_hints = {
        "redteam": "Offensive security team simulating attacks",
        "blueteam": "Defensive security team protecting systems",
        "phishing": "Fraudulent attempts to obtain sensitive information",
        "firewall": "A network security system monitoring incoming and outgoing traffic",
        "malware": "Malicious software designed to harm or exploit",
        "encryption": "The process of converting data into a secure format",
        "honeypot": "A decoy system to lure attackers and monitor them",
        "zero-day": "A vulnerability that is unknown to vendors and not yet patched",
        "penetration": "Testing a computer system for vulnerabilities",
        "botnet": "A network of infected devices controlled by an attacker"
    }

    def play_game():
        word, hint = random.choice(list(words_with_hints.items()))  # Select a random word and hint
        word_letters = set(word)  # Letters in the word
        guessed_letters = set()   # Player's guessed letters
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        lives = 7  # Number of lives

        hangman_pics = ["""
            +---+
            |   |
                |
                |
                |
                |
          =========
        """, """
            +---+
            |   |
            O   |
                |
                |
                |
          =========
        """, """
            +---+
            |   |
            O   |
            |   |
                |
                |
          =========
        """, """
            +---+
            |   |
            O   |
           /|   |
                |
                |
          =========
        """, """
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
          =========
        """, """
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
          =========
        """, """
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
          =========
        """]
        
        # Helper function to display current word progress
        def display_word():
            return " ".join([letter if letter in guessed_letters else "_" for letter in word])

        # Main game loop
        while len(word_letters) > 0 and lives > 0:
            print(f"\nYou have {lives} lives left.")
            print(hangman_pics[7 - lives])  # Display hangman status
            print("Word:", display_word())
            print(f"Hint: {hint}")  # Display the hint for the word
            print("Guessed letters:", " ".join(guessed_letters))

            # Get the player's guess
            guess = input("Guess a letter: ").lower()

            if guess in alphabet - guessed_letters:
                guessed_letters.add(guess)

                if guess in word_letters:
                    word_letters.remove(guess)
                    print(f"Good job! {guess} is in the word!")
                else:
                    lives -= 1
                    print(f"Oops! {guess} is not in the word. You lost a life loser")
            elif guess in guessed_letters:
                print("You've already guessed that letter loser")
            else:
                print("Invalid input. Please enter letters only")

        # Game over - Win or lose
        if lives == 0:
            print(hangman_pics[6])
            print(f"Game over! The word was: {word}, You smuck")
        else:
            print(f"Congratulations! You've guessed the word: {word}")

    # Loop the game until the player chooses to exit
    while True:
        play_game()
        # Ask the player if they want to play again
        choice = input("Try again? Press 'y' for yes or 'x' to exit: ").lower()
        if choice == 'x':
            print("Thanks for playing! Dev by someflavor")
            break

# Run the game
if __name__ == "__main__":
    hangman()