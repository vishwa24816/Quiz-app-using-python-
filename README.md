# Quiz App Using Python (Django)

This is a Django-based web application that generates quiz questions from a user-submitted paragraph using spaCy NLP.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishwa24816/Quiz-app-using-python-
   cd Quiz-app-using-python-
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python3 -m spacy download en_core_web_sm
   ```

4. **Apply migrations:**
   ```bash
   cd quizproject
   python3 manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

6. **Access the app:**
   Open your browser and go to [http://localhost:8000/](http://localhost:8000/) or [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Features
- Submit a paragraph and generate quiz questions using NLP.
- Three question generation strategies: extract, convert, and advanced (placeholder).
- Modern, aesthetic UI with custom CSS.

## Notes
- Make sure you have Python 3.8 or higher installed.
- For production, set `DEBUG = False` in `quizproject/settings.py` and configure allowed hosts.