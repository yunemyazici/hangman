import random
from words import words
import re

def hangman():
    attempt = 0
    vowel_count = 0
    consonant_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    secret_word = random.choice(words)
    secret_list = []
    guessed_letters = []
    hidden = "_" * len(secret_word)
    for i in range(len(secret_word)):
        secret_list.append(secret_word[i])
    for x in secret_list:
        if x in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    user_letter = None
    print(f"The secret word contains {vowel_count} vowels and {consonant_count} consonants.")
    while (attempt < 10):
        if "_" in hidden:
            print(f"Remained attemps: {10-attempt}")
            user_letter = input("\nGuess a letter: ")
            test = re.search("^[a-zA-Z]$", user_letter)
            if test:
                if user_letter not in guessed_letters:
                    guessed_letters.append(user_letter.lower())
                    for x in range(len(secret_list)):
                        if secret_word[x] == user_letter:
                            hidden = hidden[:x] + user_letter + hidden[x + 1:]
                    attempt += 1
                    print("Guessed letters: ", end="")
                    for letter in guessed_letters:
                        print(f"{letter} ",end="")
                    print(f"\n{hidden}")
                else:
                    print("You've already guessed this letter.")
            else:
                print("Guess a letter from a to z")
                pass         
        else:
            print(f"Congratulations. You won. Used attempt(s):{attempt}")
            break
    else:
        print(f"You are out of attempt. the secret word was {secret_word}")



if __name__ == "__main__":
    hangman()
