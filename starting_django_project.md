
# HOW TO START DJANGO PROJECT              


    1. create new folder         

```
mkdir new_webapp
cd new_webapp
```


    2. start virtualenv

```
virtualenv env
```

    3. activate env

```
source env/bin/activate
```

    4. installing django

```
pip install django
```

    5. making sure django is installed and creating requirements.txt

```
pip freeze
pip freeze > requirements.txt
```

    6. starting a project

```
django-admin startproject project
```

    7. creating database

```
cd project
python manage.py migrate
```

    8. starting server

```
python manage.py runserver
```

    9. go to your browser enter the server ip from terminal



```
http://127.0.0.1:8000/ 

```
