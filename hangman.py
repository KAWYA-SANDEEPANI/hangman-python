import random

# word choices
choices = ("coconut","elephant","apple","house","motorcycle","hand",
           "mobile","monkey","frock","design","monster","chocolate",
           "fisherman","watch","computer")

# selection of word
word = random.choice(choices)
wrong = 0  # count wrong guesses

# hangman stages
stages = [
"""
   -----
   |   |
       |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
       |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
---------
""",
"""
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
---------
"""
]

# game loop
while wrong < len(stages) - 1:
    print("\nGUESS A LETTER:")
    letter = input()

    if letter in word:
        print("YES")
        print("The index of letter", letter, "is", word.index(letter))
    else:
        print("NO")
        wrong += 1
        print(stages[wrong])

# game over
print("HANGMAN COMPLETE!")
print("You lost!")
print("Hidden word is:", word)