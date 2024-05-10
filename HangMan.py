import random
from nltk.corpus import words

wordList=words.words()
word=random.choice(wordList)
word=word.lower()

print("Welcome to Hangman game\nUse only lowercase letters: GOOD LUCK!")

guess="-"*len(word)
lives=6

hang='''         +---------|
         |         |
                   |
                   |
                   |
                   |'''

wordList=list(word)
guessList=list(guess)

while lives!=0:
    wrong=True
    print(hang)
    print(f"You have {lives} lives remaining")
    print(f"\n{guess}\n")
    letter=input("Enter a letter : ")
    for x in range(len(word)):
        if wordList[x]==letter:
            guessList[x]=letter
            wrong=False
            guess="".join(guessList)
    if guess==word:
        print(guess)
        print("You Won!!")
        break
    if wrong==True:
        lives=lives-1
        if lives==5:
            hang='''                     +---------|
                     |         |
                     O         |
                               |
                               |
                               |'''
        elif lives==4:
            hang='''                     +---------|
                     |         |
                     O         |
                     |         |
                               |
                               |'''
        elif lives==3:
            hang='''                     +---------|
                     |         |
                     O         |
                    \\|         |
                               |
                               |'''
        elif lives==2:
            hang='''                     +---------|
                     |         |
                     O         |
                    \\|/        |
                               |
                               |'''
        elif lives==1:
            hang='''                     +---------|
                     |         |
                     O         |
                    \\|/        |
                     |         |
                    /          |'''
        elif lives==0:
            hang='''                     +---------|
                     |         |
                     O         |
                    \\|/        |
                     |         |
                    / \\        |'''
        else:
            print("You are a hacker!!")
            lives=0
else:
    print(hang)
    print(f"The word was {word}")
    print("You loose!!")
input("Press any key to continue...")
                