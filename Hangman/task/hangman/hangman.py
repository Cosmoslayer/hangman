# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
hint_word = "-" * (len(random_word))
letters_list = list(random_word)
guessed_letters = set()
wrong_letters = set()
tries = 8
print("H A N G M A N")
while tries > 0:
    print(f"\n{hint_word}")
    answer = input("Input a letter: ")
    if len(answer) > 1:
        print("You should input a single letter")
    elif answer.isupper() or not answer.isalpha():
        print("Please enter a lowercase English letter")
    else:
        if answer not in random_word:
            if answer in wrong_letters:
                print("You've already guessed this letter")
            else:
                wrong_letters.add(answer)
                print("That letter doesn't appear in the word")
                tries -= 1
        else:
            if answer in guessed_letters:
                print("You've already guessed this letter")
            else:
                guessed_letters.add(answer)
                for i in range(len(letters_list)):
                    if letters_list[i] == answer:
                        position = i
                        hint_word = hint_word[:position] + answer + hint_word[position + 1:]
                if "-" not in hint_word:
                    print(f"You guessed the word {random_word}!\nYou survived!")
                    break

else:
    print("You lost!")
