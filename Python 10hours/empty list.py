import random
import time

wordlist = ['bug', 'bounty', 'random']

print('Welcome to the Game! ')
time.sleep(1)
print('............')
print('this is a game and you have to guess a letter')

secret_word = random.choice(wordlist)
get_word = []

for letter in secret_word:
    get_word += '_'
print(get_word)

max_attempts = 6
attempts_count = 0

while attempts_count < max_attempts:
    letter_user = input('guess a letter: ')
    letter_user.lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == letter_user:
            get_word[position]= letter

if get_word == secret_word:
    print('congratulations! you win')

attempts_count += 1

print(get_word)
print(f'Attempts:{attempts_count}/{max_attempts}')

if attempts_count == max_attempts:
    print('You have exceeded the maximum number of attempts')
    print('the secret word was: ', secret_word)

