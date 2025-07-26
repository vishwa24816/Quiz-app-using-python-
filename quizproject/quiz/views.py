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

    # 1. Show all sentences as questions
    for sent in doc.sents:
        questions.append(sent.text.strip())

    # 2. Simple rule: turn statements into questions (add '?')
    simple_questions = []
    for sent in doc.sents:
        text = sent.text.strip()
        if not text.endswith('?'):
            simple_questions.append(text + '?')
        else:
            simple_questions.append(text)

    # 3. Placeholder for advanced NLP-based question generation
    # Replace this with your own logic or a library call
    advanced_questions = [f"(NLP) What is a possible question for: '{sent.text.strip()}'?" for sent in doc.sents]

    # Choose which method to use (uncomment as needed)
    # questions = questions  # All sentences as questions
    # questions = simple_questions  # Statements turned into questions
    # questions = advanced_questions  # Placeholder for advanced NLP

    # For demo, show all three in the template
    return render(request, 'quiz/generate_quiz.html', {
        'questions': questions,
        'simple_questions': simple_questions,
        'advanced_questions': advanced_questions,
    })
