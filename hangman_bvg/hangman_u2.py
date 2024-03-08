"""
Tkinter with https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_pack.wp


import random
import django.contrib.messages


# Initialize variables
word_list = ['PANKOW', 'GÖRLITZER BAHNHOF']
the_word = None
guessed = []
numberOfGuesses = 0
  
def newGame():
    global the_word, guessed, numberOfGuesses
    the_word = random.choice(word_list)
    guessed = ['_' for _ in the_word]  # Initialize guessed letters with underscores
    numberOfGuesses = 0
    update_display()
    
def update_display():
    lblWord.set(' '.join(guessed))

def guess():
    letter = guessedLetter.get().upper()
    if len(letter) != 1:
        #messages.add_message(request, messages.INFO, "Attention, il ne faut renseigner qu'une seule lettre à la fois.")
        global numberOfGuesses
        if numberOfGuesses < 6:
            if letter in the_word:
                for idx, char in enumerate(the_word):
                    if char == letter:
                        guessed[idx] = letter
                update_display()
                if '_' not in guessed:
                    "bravo = messagebox.askquestion("BRAVO ! ✨", "Félicitations ! Tu as trouvé la station mystère ! Souhaites-tu recommencer un nouveau jeu ?")
                    if bravo == 'yes':
                        newGame()  # Start a new game if 'yes' is chosen
                    else:
                        window.quit()  # Quit the game if 'no' is chosen)
                        
        else:
            #messagebox.showerror("Dommage 🤔","Malheureusement, la station mystère ne contient pas cette lettre.")
            numberOfGuesses += 1
            update_display()
            #if numberOfGuesses == 6:
                #lost = messagebox.askquestion("C'est perdu", "Malheureusement, tu n'as pas trouvé la station mystère. Souhaites-tu recommencer un nouveau jeu ?")
                #if lost == 'yes':
                    #newGame()  # Start a new game if 'yes' is chosen
                #else:
                    #window.quit()  # Quit the game if 'no' is chosen
   # else:
        #messagebox.showinfo("Game Over", "You have already used up all your guesses.")
        
        # Clear the entry field after clicking Submit button
    #letter.delete(0, 'end')

# UI elements
guessedLetter = input().lower()
lblWord = input().lower()


# Launch the game
newGame()
"""