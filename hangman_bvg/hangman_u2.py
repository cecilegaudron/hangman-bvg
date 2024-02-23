"""
Tkinter with https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_pack.wp

"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random

window = tk.Tk()

# Initialize variables
word_list = ['PANKOW']
the_word = None
guessed = []
numberOfGuesses = 0

# Window's size, position and background color. Define a title
window.geometry("1000x400+50+50")
window.attributes("-topmost", 1)
window.config(bg = "#f0d722")
window.title('BAHNHOF U1')

    
def newGame():
    global the_word, guessed, numberOfGuesses
    the_word = random.choice(word_list)
    guessed = ['_' for _ in the_word]  # Initialize guessed letters with underscores
    numberOfGuesses = 0
    update_display()
    
def update_display():
    lblWord.set(' '.join(guessed))
    bottom_label.config(text=f"{numberOfGuesses}/6 essais")

def guess():
    letter = guessedLetter.get().upper()
    if len(letter) != 1:
        warning_message = messagebox.showwarning(
              "Attention ! ⚠", 
              "Attention, il ne faut renseigner qu'une seule lettre à la fois.",
              )
        return
    global numberOfGuesses
    if numberOfGuesses < 6:
        if letter in the_word:
            for idx, char in enumerate(the_word):
                if char == letter:
                    guessed[idx] = letter
            update_display()
            if '_' not in guessed:
                bravo = messagebox.askquestion("BRAVO ! ✨", "Félicitations ! Tu as trouvé la station mystère ! Souhaites-tu recommencer un nouveau jeu ?")
                if bravo == 'yes':
                    newGame()  # Start a new game if 'yes' is chosen
                else:
                    window.quit()  # Quit the game if 'no' is chosen)
        else:
            messagebox.showerror("Dommage 🤔","Malheureusement, la station mystère ne contient pas cette lettre.")
            numberOfGuesses += 1
            update_display()
            if numberOfGuesses == 6:
                lost = messagebox.askquestion("C'est perdu", "Malheureusement, tu n'as pas trouvé la station mystère. Souhaites-tu recommencer un nouveau jeu ?")
                if lost == 'yes':
                    newGame()  # Start a new game if 'yes' is chosen
                else:
                    window.quit()  # Quit the game if 'no' is chosen
    else:
        messagebox.showinfo("Game Over", "You have already used up all your guesses.")
        
        # Clear the entry field after clicking Submit button
    letter_entry.delete(0, 'end')

# UI elements
guessedLetter = StringVar()
lblWord = StringVar()

top_label = Label(
      window, 
      text="La ligne U1 du métro berlinois compte 13 stations et est longue de 9,0 km.\nLa U1 est en grande partie un métro aérien surélevé,\ncette ligne représente la plus ancienne ligne de métro de Berlin.", 
      fg="black", 
      bg="#f0d722",
      font= ("Helvetica 14")
      )
top_label.pack(side="top", fill="x")
    
left_label = Label(
      window, 
      text="U1\nWarschaeur Straße\n>\nUhlandstraße", 
      fg="white", 
      bg="#7eaf4b",
      font=("Helvetica 20 bold"),
      relief='solid',   # Adding relief to simulate border-radius
      pady=70  # Increase the vertical padding to extend the color vertically
      )
left_label.pack(side="left", fill="x")
        
right_label = Button(
      window, 
      text="Nouveau\nJeu", 
      command = lambda:newGame(),
      fg="white", 
      bg="black",
      font=("Helvetica 10 bold"),
      border=5,  # Add a border
      relief=RAISED,  # Add a relief
      padx=10,  # Add horinzontal padding
      pady=5,  # Add vertical padding
      bd=4,  # Ajouter un espacement du relief
      )
right_label.pack(side="right", fill="x")

bottom_label = Label(window, text=f"{numberOfGuesses}/6 essais", font=("Helvetica 16"))
bottom_label.pack(side="bottom", fill="x")

# Define the upper top area with the guessed letters
word_display = Label(
      window, 
      textvariable = lblWord,
      fg="black", 
      bg="#f0d722",
      font=('consolas 28 bold'),
      pady=40,  # Add vertical padding
      )
word_display.pack(side="top", fill='x')
        
# Define the central area
# Define the entry area, with label, entry and submit button
entry_label = Label(
      window, 
      text="Choisir une lettre :",
      fg="black", 
      bg="#f0d722",
      font=('consolas 14 bold'),
      )
entry_label.pack()

letter_entry = Entry(
      window, 
      textvariable=guessedLetter, 
      width=10, 
      fg="black", 
      bg="white",
      font=('consolas 30 bold'),)
letter_entry.pack()
letter_entry.bind("<Return>", lambda event: guess())

submit_button = Button(
      window, 
      text="Valider", 
      command=guess,
      fg="black", 
      bg="white",
      font=('consolas 14 bold'),
      )
submit_button.pack()


# Create the window, launch the game and display it in the tkinter window
newGame()
window.mainloop()