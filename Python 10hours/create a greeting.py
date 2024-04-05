import random
import time

letterlist = ['h', 'a', 'b','m','n','k','e','y','d','c','u']
wordlist = ['bug', 'bounty', 'random']

print('Welcome to the game! ')
time.sleep(2)
print('............')
print('this is a game and you have to guess a letter, good lucky!')

random.shuffle(wordlist)

secret_word = random.choice(wordlist)

letter_user = input('guess a letter: ')
letter_user.lower()

if letter_user in secret_word:
    print(f'you are good!!, the selected word was: {secret_word}')
else:
    print(f'oh no :( i doesnt have this letter, the chosen word was: {secret_word}')