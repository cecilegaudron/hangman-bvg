from django.db import models
import json

class Guess(models.Model):
    userLetterChoice = models.CharField(
        "Einen Buchstaben auswählen:", 
        default = '',
        max_length=1,
        null=False,
        blank=False
        )
    userChoice = models.JSONField(default=list)
    lives = models.IntegerField(default=6)
    
    def get_userChoice(self):
        return json.loads(self.userChoice)
    
    def set_userChoice(self, userChoice):
        self.userChoice = json.dumps(userChoice)
