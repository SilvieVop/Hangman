# Hangman animals
import random
from _2_stages_of_hangman import stages

print(f"HELLO MY FRIEND\n"
      f"Welcome in my second pygame name HANGMAN with animals... grrrrr\n"
      f"You have 6 lives to the start."
      f" \nAuthor: Silvie Vopatová")

# Generování náhodné slova, list - jestli budeš rozšiřovat list, bude dobré,
# udělat si další soubor a pak je ho sem importovat
words = ["dog", "cat", "duck", "owel", "monkey", "shark",
        "squirrel", "pig", "hen", "caterpillar", "butterfly", "fish", "mouse",
        "goat", "crab", "crocodile", "giraffe", "lion", "tiger", "penguin", "snake"]

random_word = words[random.randint(0, 20)]

# Generování podrtržítek - zde by pak mělo být vykreslení, podrtžítek v pygame
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_") # dosazení podtržítek místo písmen
#print(hidden_word)

# omezení počtu pokusů
lives = 6
print(stages[6])


# zatím jednodušší to sem dát po druhé.. vypsání
printedWord = ""  # tohle už je string není to LIST!!!
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)


# Hádaní uživatele opakované - WHILE LOOP
while "_" in hidden_word: # cyklus opakování
    guess = input(f"Guess animal. Choose the letter\n").lower() # i když zadá velké lower zajistí malé
    for index in range(0, len(random_word)): # generuj od nuly do délky hledaného slova
        if guess == random_word[index]:
            hidden_word[index] = guess

    # kontrola životů
    if guess not in random_word: # random_word je string!!
        lives -= 1
        print(stages[lives])
    print(f"The number of your lives is {lives}")
    if lives == 0:
        print(f"GAME OVER!!!")
        break # tohle zastaví  cyklus a pojedeme dál.

# vypsání do normální podoby jen převod nic víc to nedělá - už nebudou ty podrtžítky v uvozovkách
    printedWord = "" # tohle už je string není to LIST!!!
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)

# ctrl shift P - když potřebuji Killnout ten program - relange active terminal - alt b

# kontrola výhry - kontrola jestli je tam podrtžítko, když ne tak nevyhrál
    if "_" not in hidden_word:
        print(f"YOU WIN!")

