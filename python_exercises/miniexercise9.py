import random
import time
print("WELCOME TO HANGMAN CHALLENGE")
name=input("Enter Your Name:")
print("Hello "+name+".Game about to start all the best  ")
time.sleep(3)
def main():
    global count
    global  display
    global word
    global play_game
    global length
    global already_guessed
    wtg=["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"]
    word=random.choice(wtg)
    length=len(word)
    count=0
    display = '_ ' * length
    already_guessed = []
    play_game = ""
def loop():
    global play_game
    play_game=input("wanna play again?????????Y or n")
    if(play_game=='y'):
        main()
    else :
        print("thank you")
        exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("it has  " + display + " letters\n "+" Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_"+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display+"\n")
    elif guess in already_guessed:
        print("enter any other letter")
    else:
        count=count+1
        if count==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        if count==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:"+already_guessed[])
            loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        loop()
    elif count != limit:
        hangman()
main()
hangman()
