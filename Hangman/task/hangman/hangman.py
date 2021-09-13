# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
hint_word = random_word[0:3] + "-" * (len(random_word) - 3)
print("H A N G M A N")
answer = input(f"Guess the word: {hint_word}")
if answer == random_word:
    print("You survived!")
else:
    print("You lost!")
