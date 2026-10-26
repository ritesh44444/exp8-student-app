# Experiment 8 — Retrieve Student Information with SQLite

This experiment contains two separate implementations:
1. Flask + SQLite
2. Django + SQLite

Both applications create a student table, insert sample records, and display student information from the database.

## Requirements
- Python 3.10+
- Git
- GitHub account and a repository created on GitHub (for CLI upload)

---

## Part A: Flask

Open a terminal and enter the Flask folder:

```bash
cd flask_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

The app creates `students.db` automatically and inserts sample data if the table is empty.

Stop the server with `Control + C`.

## Part B: Django

From the project root, enter the Django folder:

```bash
cd django_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python seed_students.py
python manage.py runserver
```

Open http://127.0.0.1:8000

The app creates the database schema through Django migrations and inserts sample records if no students exist.

Stop the server with `Control + C`.

---

## Upload to GitHub through CLI

1. Create an **empty repository** on GitHub (do not add README or .gitignore there).
2. From the extracted `exp8_flask_django_sqlite` root folder, run:

```bash
git init
git add .
git commit -m "Add Experiment 8 Flask and Django SQLite apps"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your GitHub username and repository name.

If Git says `remote origin already exists`, use:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

If Git asks you to authenticate, complete the browser sign-in prompt or use a GitHub-supported authentication method. Your GitHub account password is not accepted for HTTPS Git operations.

## What the code demonstrates
- Connecting to SQLite
- Creating and reading student records
- Flask route and HTML template
- Django model, view, URL routing, and template
- Uploading a project using Git CLI

Do not commit virtual environments, local database files, secrets, or access tokens.
