Cy Career Expart Project Setup Guide:
Clone the repository:
Development Environment Setup:
Python Version: Ensure Python 3.8 is installed.

Node.js Version: You’ll need Node.js 18.17.0. Use NVM (Node Version Manager) to switch between Node.js versions if working on multiple projects.

Dependency Management: I used pipenv.
Installing Dependencies:
pipenv shell
pipenv install
Setting Up the Environment Variables:
"""
    We are using django-env to get enviromnet variable.
    More details can be found here: https://django-environ.readthedocs.io/en/latest/
"""

DEBUG=True
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,
DEVELOPMENT_SERVER=True

DATABASE_URL=postgres://username:password@172.17.0.1:5432/mce
SECRET_KEY=
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=

Running the Project:
Apply migrations:
python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py createsuperuser

Start the server:
python3 manage.py runserver



