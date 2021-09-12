# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
print("H A N G M A N")
answer = input("Guess the word:")
if answer == random_word:
    print("You survived!")
else:
    print("You lost!")
