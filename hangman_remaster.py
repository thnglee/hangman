import random 

def get_source(): 
    f = open('source.txt','r',encoding='utf-8')
    return f.read()

def get_wordslist(content):
    return content.split()

class hangman(): 
    def __init__(self,word): 
        self.word = word
        self.word_completion = '_'*len(self.word)
    def partial_reveal(self,char): 
        chars_list = list(self.word)
        dash_list = list(self.word_completion)
        indices = [i for i,letter in enumerate(chars_list) if char == letter]
        for value in indices: 
            dash_list[value] = char
        self.word_completion = ''.join(dash_list)
    def display(self,chance_left): 
        print(self.word_completion)
        print(chance_left)
    def checking(self): 
        if self.word_completion == self.word: 
            return True 
        else: 
            return False

def main(): 
    content = get_source()
    wordslist = get_wordslist(content)
    guessed = False
    chance_left = 6
    # creating object: 
    word = random.choice(wordslist)
    core = hangman(word)

    while not guessed and chance_left > 0: 
        core.display(chance_left)
        user_input = str(input("Input a char to guess: "))
        if user_input in word: 
            core.partial_reveal(user_input)
        else: 
            chance_left -= 1 # initial chance left = 6

        result = core.checking()
        if result == True: 
            guessed = True

    if guessed == True: 
        print("Winner Chicken Dinner")
    else: 
        print("Loser")
        print("The word is: " + word)


if __name__ == "__main__": 
    main()
    ans_set = ['yes','y']
    while input("Wanna play again!...").lower() in ans_set: 
        main()

        
    