# import session:
import time 
import random as ran 
import os 

# GetWord function: 
def GetWord(): 
    OpeningSourceWordsFile = open('D:/Python_Project_Outline/5_Hangman/source.txt','r')
    ReadingContent = OpeningSourceWordsFile.read()
    WordsList = ReadingContent.split()
    return ran.choice(WordsList)

# introduction to the game
def greeting(): 
    print()
    print("Welcome to the Hangman game...")
    print("created by: thanglee... 2020")
    print("Enjoy and have a nightmare...")
    print()
    print("you have 6 chances to guess a word, and each time you fail...")
    print("your partner get closer to the death...")
    input("so try your best, ok ?")
    clear()

# function to clear the screen in window
def clear(): 
    os.system('cls')
    # clear the console screen

# play function:
def play(word): 
    # get the random word from the file 
    TargetWord = word.upper()

    # word completion: 
    WordCompletion = "_" * len(TargetWord)
    
    # ChanceLeft: 
    ChanceLeft = 6

    # Dulicated Data session: 
    TriedInput = []
    
    # initial display: 
    print()
    print("There are " + str(len(TargetWord)) + " letters in this word")
    DisplayHangman(ChanceLeft)
    print(WordCompletion)

    # exceptional handling and executing code 
    try: 
        # Loop Session: 
        while ChanceLeft > 0: 
            # UserInput session: 
            print("\n")
            UserInput = input("Input a character or input a word to guess: ").upper()
            print()

            # Duplicate database checking
            if not UserInput in TriedInput:
                # Input 1 letter:
                if len(UserInput) == 1 and UserInput.isalpha() == True: 
                    # Status: Right letters
                    if UserInput in TargetWord:
                        print("Bingo, this word has the letter: " + UserInput)
                        TriedInput.append(UserInput)
                        # Revelation session (include initial start point): 
                        WordCompletion = PartialReveal(UserInput, TargetWord, WordCompletion)
                    # Status: Wrong letters 
                    else: 
                        print("the word doesn't have letter: " + UserInput)
                        TriedInput.append(UserInput)
                        ChanceLeft -= 1
                # Input the whole word: 
                elif len(UserInput) > 1 and UserInput.isalpha() == True: 
                    if UserInput == TargetWord: 
                        print("you won") 
                        break
                    # not the right word guessing
                    else: 
                        print(UserInput + " is not the right word")
                        TriedInput.append(UserInput)
                        ChanceLeft -= 1
                # Wrong input situation:
                else:   
                    print("Invalid Input")
                    print("English words can not contain numbers and other specific characters ! ")

                # winning statement condition: 
                if not '_' in WordCompletion: 
                    print("you are the winner") 
                    break
                # display is not winning
                print()
                DisplayHangman(ChanceLeft)
                print()
                print("ChanceLeft: " + str(ChanceLeft))
                print()
                print(WordCompletion)
                print()
            # Duplicated Tried word handling
            else: 
                print("you have had input this word or letters before !")
                print("ChanceLeft: " + str(ChanceLeft) + " (the same - i don't want to prevent you from winning...)")
        # Losing statement
        else: 
                print("You lost - The right word is: " + TargetWord)
                print("anyway, nice try - loser !!!")
    except KeyboardInterrupt: 
        ans_set = ['yes','Y','y']
        print()
        if input("Do you wish to proceed action? [y/n]: ") in ans_set: 
            exit()
        else: 
            pass
    else: 
        pass
# Display Hangman:
def DisplayHangman(ChanceLeft): 
    if ChanceLeft == 0: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print(r"  / \  ")
    elif ChanceLeft == 1: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print("  /    ")
    elif ChanceLeft == 2: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print("       ")
    elif ChanceLeft == 3: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("       ")
        print("       ")    
    elif ChanceLeft == 4: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"   |\  ")
        print("       ")
        print("       ")
    elif ChanceLeft == 5: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print("   |   ")
        print("       ")
        print("       ")
    elif ChanceLeft == 6: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print("       ")
        print("       ")
        print("       ")


# Partial Reveal - Core of the program: 
def PartialReveal(UserInput, TargetWord, WordCompletion): 
    
    LetterSep = list(TargetWord)
    
    WordCompletion_DashSep = list(WordCompletion)
    indices = [i for i, letter in enumerate(LetterSep) if UserInput == letter]
    for value in indices: 
        WordCompletion_DashSep[value] = UserInput
    '''
    for index in range(len(TargetWord)): 
        if LetterSep[index] == UserInput: 
            WordCompletion_DashSep[index] = UserInput

    '''
    WordCompletion_Done = "".join(WordCompletion_DashSep)
    return WordCompletion_Done

# main function: 
def main(): 
    greeting()
    word = GetWord()
    play(word)
    ans_set = ['yes', 'y', 'Y']
    while input("Play Again ? [Y/N] ...") in ans_set:
        clear()
        word = GetWord()
        play(word)
    else: 
        exit()

# main executing function:
if __name__ == "__main__":
    main()