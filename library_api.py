django-admin startproject library_api
cd library_api
python manage.py startapp library_app
pip install djangorestframework

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
