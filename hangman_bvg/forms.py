from django import forms
from .models import Guess

# Form for the user to make a guess
class GuessForm(forms.ModelForm):
    class Meta:
        model = Guess
        fields = ('userLetterChoice',)
        
    def __init__(self, *args, **kwargs):
        super(GuessForm, self).__init__(*args, **kwargs)
