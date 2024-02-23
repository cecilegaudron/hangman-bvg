from django.shortcuts import render
from django.http import JsonResponse

from .hangman_u2 import newGame, window

def index(request):
    """ Basic view for Home Page"""
    return render(request, 'hangman_bvg/index.html')

def game_u1(request):
    newGame()
    window.mainloop()
    
    return render(request, 'game_u1')
    #result = "Code Python exécuté avec succès!"
    #return JsonResponse({'result': result})