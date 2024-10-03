import random
steps = ['''
 +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["almonds","cashew","oats" ]
lives = 6
chosen_word= random.choice(word_list)
print(chosen_word)



placeholder = ""
word_length = len(chosen_word)
for positon in range(word_length):
    placeholder += ""
print(placeholder)

game_over = False
correct_letter =[]

while not game_over:
    guess = input("Guess a letter :").lower()



    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"


    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose.")


    if "_" not in display:
        game_over = True
        print("you win.")
    print(steps[lives])