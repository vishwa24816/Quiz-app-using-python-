from django import forms
from .models import Quiz

class ParagraphForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['paragraph']
