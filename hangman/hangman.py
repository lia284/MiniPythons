import random
import numpy
from words import words

def getWord():
    word = random.choice(words)
    return word.upper()

def play(word):
    lines = "_" * len(word)
    win = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Welcome to Hangman!")
    print(showHangman(tries))
    print(lines)
    print("\n")

    while not win and tries > 0:
        user_input = input("Enter a letter: ").upper()
        print(user_input)
        if len(user_input) == 1 and user_input.isalpha():
            if user_input in guessedLetters:
                print("You already guessed that letter")
            elif user_input not in word:
                print("This letter is not in the word")
                tries -= 1
                guessedLetters.append(user_input)
            else:
                print(user_input, " is in the word.")
                guessedLetters.append(user_input)
                wordAsList = list(lines)
                indices = [i for i, letter in enumerate(word) if letter == user_input]
                for index in indices:
                    wordAsList[index] = user_input
                lines = "".join(wordAsList)
                if "_"  not in lines:
                    win = True
        elif len(user_input) == len(word) and user_input.isalpha:
            if user_input in guessedWords:
                print("You already guessed the word.")
            elif user_input != word:
                print("This is not the word")
                tries -= 1
                guessedWords.append(user_input)
            else:
                win = True
                lines = word

        else:
            print("Try again.")

        print(showHangman(tries))
        print(lines)
        print("\n")

    if win:
        print("Congratulations! You guessed the right word")
    else:
        print("You ran out of tries. The word was", word)



def showHangman(tries):
    phases = [
        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         /|\\
            |        / | \\
            |          |
            |         / \\
            |        /   \\
            |
          
        """,
        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         /|\\
            |        / | \\
            |          |
            |         / 
            |        /   
            |
          
        """,

        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         /|\\
            |        / | \\
            |          |
            |         
            |           
            |
         
        """,

        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         / \\
            |        /   \\
            |          
            |         
            |         
            |
          
        """,

        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         / 
            |        /   
            |          
            |         
            |         
            |
         
        """,

        """
            _ _ _ _ _ _
            |          |
            |          |
            |         ( )
            |         
            |         
            |          
            |         
            |         
            |
         
        """,

        """
            _ _ _ _ _ _
            |          |
            |         
            |        
            |         
            |         
            |          
            |         
            |         
            |
        """

    ]
    return phases[tries]


def main():
  word = getWord()
  play(word)
  while input("Play again? (Y/N)").upper() == "Y":
    word = getWord()
    play(word)
        

if __name__ == "__main__":
    main()
