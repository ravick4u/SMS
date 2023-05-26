- Create virtual environment
py -m venv .venv

- activate virtual environment
.\.venv\Scripts\activate

- install Django and Django REST Framework
pip install django djangorestframework

above command will install below packages

asgiref==3.7.1
Django==4.2.1
djangorestframework==3.14.0
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3

- save all packages to requirements file
pip freeze > .\requirements.txt

- Create a new project
django-admin startproject myproject