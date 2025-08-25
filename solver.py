import math

def isValid(prompt: str, feedback: list, word: str) -> bool:
    word = list(word)
    for i in range(len(feedback)):
        if feedback[i] == 'g':
            if prompt[i] != word[i]:
                return False
            word[i] = '*'
    for i in range(len(feedback)):
        if feedback[i] == 'y':
            if prompt[i] == word[i] or prompt[i] not in word:
                return False
            word[word.index(prompt[i])] = None
        if feedback[i] == 'b':
            if prompt[i] in word:
                return False
    return True


def generateFeedback(guess: str, word: str) -> list:
    feedback = ['b'] * 5
    word_list = list(word)
    for i in range(5):
        if guess[i] == word[i]:
            feedback[i] = 'g'
            word_list[i] = None
    for i in range(5):
        if feedback[i] == 'b' and guess[i] in word_list:
            feedback[i] = 'y'
            word_list[word_list.index(guess[i])] = None
    return feedback

feedback_arr = ['b', 'y', 'g']  # b-black, y-yellow, g-green


def generateGuesses(wordlist: list) -> str:
    maxentropy = -1
    bestword=""
    for word in wordlist:
        entropy = 0
        freq = {}
        for w in wordlist:
            feedback = ''.join(generateFeedback(word, w))
            if feedback not in freq:
                freq[feedback] = 0
            freq[feedback] += 1
        for f in freq:
            p = freq[f] / len(wordlist)
            entropy -= p * math.log2(p)
        if entropy > maxentropy:
            maxentropy = entropy
            bestword = word

    return bestword

'''Example usage in a console application
with open('valid-wordle-words.txt', 'r') as f:
    wordlist = [line.strip() for line in f.readlines()] 

curr_guess="tares"
while(True):
    print("Current Guess: ", curr_guess)
    feedback = input("Enter feedback (b-black, y-yellow, g-green): ")
    wordlist = [word for word in wordlist if isValid(curr_guess, feedback, word)]
    print("Possible words left: ", len(wordlist))
    if len(wordlist) <= 20:
        print(wordlist)
    if len(wordlist) <= 1:
        print("The word is: ", wordlist[0])
        break
    curr_guess = generateGuesses(wordlist)
'''



