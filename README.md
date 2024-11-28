# Steps to set up a Django Rest framework with vue
This project is for learning purposes. 
It shows how to set up Django REST with Vue according to the youtube channel [código para principiantes](https://www.youtube.com/playlist?list=PLxooeC3-xaNfS7jgZvVUM-kUcrUbgHTWJ).  


## General Project setup
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
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create a super user
```bash
python3 manage.py createsuperuser
```


## REST framework setup
To make the data of the data base readable by the Django REST Framework, they need to be serialized.

-Add a serializer class for your models to `serializers.py`.

-Generics: Add two functions to cover basic CRUD operations to `views.py`.

-ViewSet: Similar to generics, but covers basic CRUD operations with one function

-Add urls to `urls.py` (project and app).

## Vue setup

Confirm that node.js is installed correctly.
https://nodejs.org/en/download/package-manager
```bash
node -v
npm -v
```
Install vue.

https://cli.vuejs.org/guide/installation.html
```bash
npm install -g @vue/cli
vue --version
```

Create a vue 3 project within your Django project.

https://cli.vuejs.org/guide/creating-a-project.html
```bash
vue create vue-django
```
Select 
-Vue 3
-Babel
-Vuex 
-Router (history mode)
-Linter/Formatter

Run server
```bash
npm run serve
```

## Set up Django + Vue.js with Axios
```bash
cd vue-django
npm install axios
```

To avoid CORS errors we need to install django-cors-headers in our project.

Follow the instructions: 
https://pypi.org/project/django-cors-headers/

```bash
python3 -m pip install django-cors-headers
```

Modify
- INSTALLED_APPS
- MIDDLEWARE
- CORS_ALLOWED_ORIGINS
- CORS_ALLOW_METHODS

in the `settings.py` file of your Django project. 
It is not necessary to authorize Regexes.

Example for a simple API call with axios:
```bash
data() {
    return {
      categories: [],
    };
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/categories/")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
```

## Other functionalities

### Accessing data from other models
To display data from related models (for example: models connected via foreign keys), use the `ReadOnlyField` in your serializer.

### Filtering per category

Install Django filer and add to `INSTALLED_APPS`.

https://pypi.org/project/django-filter/

```bash
pip install django-filter
```

Like indicated in the [Django REST documentation](https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends), add the `DEFAULT_FILTER_BACKENDS` setting to the `settings.py` of the django project.

Then add the filters to the serializers, as described in pypi. 

```bash
from django_filters import rest_framework as filters
```