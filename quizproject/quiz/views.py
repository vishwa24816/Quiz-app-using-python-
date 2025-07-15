from django.shortcuts import render, redirect
from .forms import ParagraphForm
from .models import Quiz
import spacy

nlp = spacy.load('en_core_web_sm')

def paragraph_submission(request):
    if request.method == 'POST':
        form = ParagraphForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            return redirect('generate_quiz', quiz_id=quiz.id)
    else:
        form = ParagraphForm()
    return render(request, 'quiz/paragraph_submission.html', {'form': form})

def generate_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    doc = nlp(quiz.paragraph)
    questions = []
    for sent in doc.sents:
        if '?' in sent.text:
            questions.append(sent.text)
    return render(request, 'quiz/generate_quiz.html', {'questions': questions})
