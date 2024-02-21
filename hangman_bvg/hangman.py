"""
This is a hangman game made with Python
Part of day 39 of the 100 Days of Code Challenge https://replit.com/learn/100-days-of-python/hub
"""
import random

bahnhof_u1 = ["Gleisdreieck", "Görlitzer Bahnhof", "Hallesches Tor", "Kottbusser Tor", "Kurfürstendamm", "Kurfürstenstraße", "Möckernbrücke", "Nollendorfplatz", "Prinzenstraße", "Schlesisches Tor", "Uhlandstraße", "Warschauer Straße", "Wittenbergplatz"]
userChoice = []
lives = 6

station = random.choice(bahnhof_u1)

while True:
  userLetterChoice = input("Choisir une lettre : ▶ ").lower()

  # Check if letter chosen by user is already in the list
  if userLetterChoice in userChoice:
    print("Cette lettre a déjà été choisie ❗ ")
    continue

  # Save all letters that the user has chosen
  userChoice.append(userLetterChoice)

  # If loop to check if the letter is in the word
  if userLetterChoice in station:
    print("Correct! ✅ ")
  else:
    print("Eh non, cette lettre ne fait pas partie du mot. ❌")
    lives -= 1
    
  # For loop to check if every lettes have been found
  wordComplete = True
  print()
  for i in station:
    if i in userChoice:
      print(i, end="")
    else:
      print("_", end="")
      wordComplete = False
  print()

  if wordComplete:
    print(f"""BRAVO! 🎉
    Tu as gagné avec {lives} propositions restantes.""")
    exit()

  if lives <= 0:
    print(f"""Tu as épuisé toutes tes vies. 😭
    Il fallait trouver : {station}.""")
    exit()
  else:
    print(f"Encore {lives} propositions sur of 6.\n")
