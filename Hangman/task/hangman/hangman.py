# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
hint_word = "-" * (len(random_word))
letters_list = list(random_word)
letters_set = set()
tries = 8
print("H A N G M A N")
while tries > 0:
    print(f"\n{hint_word}")
    answer = input("Input a letter: ")
    if answer not in random_word:
        print("That letter doesn't appear in the word")
        tries -= 1
    else:
        if answer in letters_set:
            print("No improvements")
            tries -= 1
        else:
            letters_set.add(answer)
            for i in range(len(letters_list)):
                if letters_list[i] == answer:
                    position = i
                    hint_word = hint_word[:position] + answer + hint_word[position + 1:]
            if "-" not in hint_word:
                print(f"\n{random_word}")
                print("You guessed the word!\nYou survived!")
                break
else:
    print("You lost!")
