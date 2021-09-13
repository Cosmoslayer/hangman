# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
hint_word = "-" * (len(random_word))
letters_list = list(random_word)
letters_set = set(random_word)
tries = 8
print("H A N G M A N")
while tries > 0:
    print(f"\n{hint_word}\nInput a letter: ")
    answer = input()
    if answer not in random_word:
        print("That letter doesn't appear in the word")
    else:
        if answer in letters_set:
            for i in range(len(letters_list)):
                if letters_list[i] == answer:
                    position = i
                    hint_word = hint_word[:position] + answer + hint_word[position + 1:]
    tries -= 1
print("Thanks for playing!\nWe'll see how well you did in the next stage")
