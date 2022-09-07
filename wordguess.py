
### taking word out of list when it's chosen wordlist.remove(word)?
### pulling from a files

## important bit for removing is from the index position

choice = 'y'
wins = 0
losses = 0
while choice == 'y':
    import random
    wordlist = ['pizza','hotdog','water','pothos','rain']
    #wordlist = wordlist.remove(word)
    for i in range(len(wordlist)):
        word = (f'{random.choice(wordlist)}')

    empty = list('_'*len(word))
    life = 7

    print ('Hello. Welcome to Word Guessing Game. You have 7 lives.')

    while life >0:
        guess = str(input('Guess one letter or whole word: '))
        guess = guess.lower()

        if len(guess) == len(word) and guess != word:
            life = life-1
            print(f'Wrong word. You have {life} lives left.')
        elif guess not in word:
            life = life-1
            print(f'Letter not in word. You have {life} lives left.')

        for key, value in enumerate(list(word)):
            if guess == value:
                empty[key] = guess
        print(('').join(empty))


        
        if ('').join(empty) == word:
            wins +=1
            print(f'You guessed it The word was{word}.\n Wins: {wins} \t Losses: {losses} ')
            #wordlist = wordlist.remove(word)
            choice = input('Do you want to play again? y/n')
            break
        if guess == word:
            wins +=1
            print(f'You guessed it! The word was {word}.\n Wins: {wins} \t Losses: {losses} ')
            #wordlist = wordlist.remove(word)
            choice = input('Do you want to play again? y/n')
            break
    else:
        if life ==0:
            losses +=1
        else:
            wins +=1
        print (f'You lose! The word was {word}. Better luck next time!\n Wins: {wins} \t Losses: {losses} ')
        #wordlist = wordlist.remove(word)
        choice = input('Do you want to play again? y/n')

print('Bye')



#if guess in word:
#   index = word.find(guess)
#   empty = str(f'{empty[:index]}{guess}{empty[index+1:]}')
#   print(empty)
#issue = it did not account for duplicate letters. only first occurance.

#WHERE is IF in python