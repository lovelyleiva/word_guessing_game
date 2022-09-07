
import random

wins = 0
losses = 0
used_words=[]
max_guesses = 7

with open("words-file.txt", "r") as words_file:
    words = words_file.read()
    global words_list
    words_list = list(map(str, words.split('\n')))

def display_welcome_msg():
    print('Welcome to the Guess the Word Game!!!')
    print(f'You have a max of {max_guesses} incorrect guesses.')

display_welcome_msg()

def pick_word(words_list):
    word = random.choice(words_list)
    print('A random word has been choosen!')
    print('***Hint: '+word) #cheat so we can focus the testing
    return word

while True:
    word = pick_word(words_list)
    if word in used_words:
        print(f'Already used {word}...pick another word. Sorry!')
        continue
    used_words.append(word)
    guess_count = 0
    display_word = '_' * len(word)
    guesses = []
    while True:
        guess = input("Please enter the letter of your guess: ")
        if guess.isalpha() is False:
            print("Please enter a letter or a word!")
            continue
        if guess in guesses:
            print("You have guessed the letter(s) already. please try again!")
            continue
        guesses.append(guess)
        if guess in word:
            pos = [i for i in range(len(word)) if word.startswith(guess,i)]
            for i in pos:
                display_word = display_word[:i] + guess + display_word[i+len(guess):]
            print(f'The word: {display_word}')
            if "_" not in display_word:
                print("All letters guessed! We have a winner!")
                wins +=1
                break
        else:
            guess_count +=1
            if guess_count == max_guesses:
                print(f'Too many tries, Sorry, you loose! The word was "{word}".')
                losses +=1
                break
            print(f'Incorrect guess. You have {max_guesses - guess_count} guesses left.')

    while True:
        global play_again
        play_again = input(f'Win count: {wins} wins, {losses} losses. \nPlay again? (y/n)')
        if (play_again != 'y' and play_again != 'n'):
            print("invalid respondes. Expected 'y' or 'n'.")
        else:
            break
    if play_again == 'n': break

print('Goodbye. Thanks for playing')