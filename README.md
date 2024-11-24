## Steps to set up a Django Rest framework with vue

### Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
```

### Create a project
```bash
django-admin startproject tienda
```

### Add the rest framework to installed apps
```bash
'rest_framework'
```

### Create an app
```bash
cd tienda
python3 manage.py startapp products
```

### Add app to installed app list of project
```bash
'products
```

### Run the server
```bash
python3 manage.py runserver
```

### Migrations
python3 manage.py makemigrations
python3 manage.py migrate

### Create a super user
python3 manage.py createsuperuser

