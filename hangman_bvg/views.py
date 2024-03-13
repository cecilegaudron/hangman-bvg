from django.shortcuts import render, redirect
from .forms import GuessForm
from .stations import bahnhof_u1, bahnhof_u2, bahnhof_u3, bahnhof_u4, bahnhof_u5, bahnhof_u6, bahnhof_u7, bahnhof_u8, bahnhof_u9
import random


def index(request):
    # Basic view for Home Page
    return render(request, 'hangman_bvg/index.html', {})

def rules(request):
    # Basic view for Rules Page
    return render(request, 'hangman_bvg/regeln.html', {})

def new_game(request, list_name):
    # Get the game state from the session
    request.session['userChoice'] = []
    request.session['lives'] = 6
    request.session['all_guesses'] = []  # reset all_guesses
    # Choose the correct list of stations
    if list_name == 'u1':
        request.session['station'] = random.choice(bahnhof_u1)
    elif list_name == 'u2':
        request.session['station'] = random.choice(bahnhof_u2)
    elif list_name == 'u3':
        request.session['station'] = random.choice(bahnhof_u3)
    elif list_name == 'u4':
        request.session['station'] = random.choice(bahnhof_u4)
    elif list_name == 'u5':
        request.session['station'] = random.choice(bahnhof_u5)
    elif list_name == 'u6':
        request.session['station'] = random.choice(bahnhof_u6)
    elif list_name == 'u7':
        request.session['station'] = random.choice(bahnhof_u7)
    elif list_name == 'u8':
        request.session['station'] = random.choice(bahnhof_u8)
    elif list_name == 'u9':
        request.session['station'] = random.choice(bahnhof_u9)
    
def new_game_view(request, list_name):
    new_game(request, list_name)
    return redirect('game_view', list_name=list_name)

def game_view(request, list_name):
    # Variable to store all guesses
    if 'all_guesses' not in request.session:
        request.session['all_guesses'] = []
    # Get the game state from the session
    userChoice = request.session.get('userChoice', [])
    lives = request.session.get('lives', 6)
    if list_name == 'u1':
        station = request.session.get('station', random.choice(bahnhof_u1))
        template_name = 'hangman_bvg/hangman_u1.html'
    elif list_name == 'u2':
        station = request.session.get('station', random.choice(bahnhof_u2))
        template_name = 'hangman_bvg/hangman_u2.html'
    elif list_name == 'u3':
        station = request.session.get('station', random.choice(bahnhof_u3))
        template_name = 'hangman_bvg/hangman_u3.html'
    elif list_name == 'u4':
        station = request.session.get('station', random.choice(bahnhof_u4))
        template_name = 'hangman_bvg/hangman_u4.html'
    elif list_name == 'u5':
        station = request.session.get('station', random.choice(bahnhof_u5))
        template_name = 'hangman_bvg/hangman_u5.html'
    elif list_name == 'u6':
        station = request.session.get('station', random.choice(bahnhof_u6))
        template_name = 'hangman_bvg/hangman_u6.html'
    elif list_name == 'u7':
        station = request.session.get('station', random.choice(bahnhof_u7))
        template_name = 'hangman_bvg/hangman_u7.html'
    elif list_name == 'u8':
        station = request.session.get('station', random.choice(bahnhof_u8))
        template_name = 'hangman_bvg/hangman_u8.html'
    elif list_name == 'u9':
        station = request.session.get('station', random.choice(bahnhof_u9))
        template_name = 'hangman_bvg/hangman_u9.html'
    
    # Create a string that represents the current state of the guessed word
    # guessed_word = ''.join(letter if letter in userChoice else '_' for letter in station)
    guessed_word = ''.join(letter if letter in userChoice else ' ' if letter == ' ' else '_' for letter in station)
            
    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            userLetterChoice = form.cleaned_data.get('userLetterChoice').lower()
            
            # Update all_guesses with the new guess
            all_guesses = request.session['all_guesses']
            all_guesses.append(userLetterChoice)
            request.session['all_guesses'] = all_guesses

            # Update the game state based on the user's guess
            if userLetterChoice in userChoice:
                message = "Dieser Buchstabe wurde bereits ausgewählt ❗ "
            elif userLetterChoice in station.lower():
                message = "Richtig! ✅ "
                userChoice.append(userLetterChoice)
                if all(letter in userChoice for letter in station.lower()):
                    message = f"BRAVO! 🎉 Du hast mit {lives} verbleibenden Versuchen gewonnen!"
            else:
                message = "Nein, dieser Buchstabe ist nicht Teil des Wortes. ❌"
                lives -= 1
                if lives == 0:
                    message = f"Du hast alle deine Versuche ausgeschöpft. 😭 Wir mussten herausfinden : '{station}'."

            # Save the game state in the session so it persists across requests
            request.session['userChoice'] = userChoice
            request.session['lives'] = lives
            request.session['station'] = station

            form = GuessForm()  # create a new form instance
    else:
        form = GuessForm()
        message = None
        
    # Create a list of guessed letters that are not in the station word
    all_guesses = request.session.get('all_guesses', [])
    wrong_letters = [letter for letter in all_guesses if letter not in station]

    return render(request, template_name, {
        'form': form, 
        'message': message, 
        'userChoice': userChoice, 
        'lives': lives, 
        'station': station,
        'guessed_word': guessed_word,
        'wrong_letters': wrong_letters,
        })
    
def quit(request):
    request.session.flush()
    return redirect('index')