import random as ran

def get_word(): 
    OpeningSourceWordsFile = open('D:/Python_Project_Outline/5_Hangman/source.txt','r')
    ReadingContent = OpeningSourceWordsFile.read()
    WordsList = ReadingContent.split()
    word = ran.choice(WordsList)    
    return word.upper()

def play(word): 
    word_completion = "_" * len(word)
    guessed = False 
    guessed_letter = []
    guessed_words = []
    tries = 6
    print("let's play hangman")
    display_hangman(tries)
    print(word_completion)
    print()

# a boolean is automatically true when having the condition
    while not guessed and tries > 0: 
        guess = input("letter or word: ").upper()

        # start executing project
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("you already guessed the letter: " + guess)
            elif guess not in word:
                print(guess + " is not in the word ")
                tries -= 1
                guessed_letter.append(guess)
            else: 
                print(guess + " is in the word") 
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices: 
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

            # soon terminal testing
                if "_" not in word_completion: 
                    guessed = True
            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words: 
                print("already guessed")
            elif guess != word:
                print(guess + 'is not the word.')    
                tries -= 1
                guessed_words.append(guess)
            else: 
                guessed = True
                word_completion = word
        else: 
            print("not a valid guess")
        # printing result:  
        display_hangman(tries)
        print(word_completion)
        print()
    
    if guessed == True: 
        print("winner chickene dinner")
    else: 
        print("look at the mirror, you can see a loser")
        print("anyway, the word is: " + word )


# Display Hangman:
def display_hangman(tries): 
    if tries == 0: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print(r"  / \  ")
    elif tries == 1: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print("  /    ")
    elif tries == 2: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("   |   ")
        print("       ")
    elif tries == 3: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"  /|\  ")
        print("       ")
        print("       ")    
    elif tries == 4: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print(r"   |\  ")
        print("       ")
        print("       ")
    elif tries == 5: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print("   |   ")
        print("       ")
        print("       ")
    elif tries == 6: 
        print("----   ")
        print("   |   ")
        print("   O   ")
        print("       ")
        print("       ")
        print("       ")

def main():
    word = get_word()
    play(word)
    ans_set = ['Y','y','yes']
    while input("want to play again ?...  ") in ans_set: 
        word = get_word()
        play(word)
if __name__ == "__main__":
    main()