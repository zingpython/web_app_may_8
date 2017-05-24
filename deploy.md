Setup Django, Apache2, Python Tools, and mod_wsgi on Debian Linux Systems.

Step 1. Install Python Tools, Git, Apache2, and Mod_WSGI on your Debian Linux System

```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install git

sudo apt-get install apache2

sudo apt-get install python-pip python-virtualenv python-setuptools python-dev build-essential

sudo apt-get install libapache2-mod-wsgi-py3

sudo apt-get build-dep python-imaging

```

Step 2. Start Virtualenv and install Python3
```
sudo pip install virtualenv 

cd /var/www

mkdir venv && cd venv

virtualenv -p python3 .

source bin/activate

python --version
```

Step 3. Clone github repo
```
git clone https://github.com/zingpython/feb_webapp.git

```

Step 4.

Install all libriaries from requirements.txt
```
cd feb_webapp
pip install -r requirements.txt
```

Step 5.
You need the python pillow
```
pip install pillow
```

Step 6.
Start Django, migrate db and create super user
```
cd project
python manage.py migrate

python manage.py createsuperuser 
```

Step 7. 
Setup Static & Media Root directories.
Make sure you are in /var/www/venv/your_folder_from_github/project/
```
mkdir static
mkdir staticfiles
mkdir media
```

Step 8.
Open 000-default.conf to change Apache2 configuration
```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Step 9.
Change 000-default.conf configuration
```
<VirtualHost *:80>
ServerName localhost
ServerAdmin webmaster@localhost

Alias /static /var/www/venv/web_app_may_8/blog_project/static
<Directory /var/www/venv/web_app_may_8/blog_project/static>
   Require all granted
 </Directory>

Alias /media /var/www/venv/web_app_may_8/blog_project/media
<Directory /var/www/venv/web_app_may_8/blog_project/media>
   Require all granted
</Directory>

<Directory /var/www/venv/web_app_may_8/blog_project/blog_project>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess cfehome python-path=/var/www/venv/web_app_may_8/blog_project/:/var/www/venv/lib/python3.4/site-packages
WSGIProcessGroup cfehome
WSGIScriptAlias / /var/www/venv/web_app_may_8/blog_project/blog_project/wsgi.py


ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Step 10.
Add User Permissions (to modify sqlite3 Database).
sudo chown is a command to change the ownership of a file/folder at a time to a specified user. CHOWN stands for CHange file OWNer.
sudo chmod 755 filename command - you allow everyone to read and execute the file, and the file owner is allowed to write to the file as well. 
sudo chmod 777 means making the file readable, writable and executable by everyone.
```
sudo adduser $USER www-data
sudo chown www-data:www-data /var/www/venv/web_app_may_8/blog_project
sudo chown www-data:www-data /var/www/venv/web_app_may_8/blog_project/db.sqlite3
sudo chmod -R 775 /var/www/venv/web_app_may_8/blog_project
sudo chmod 777 /var/www/venv/web_app_may_8/blog_project/media/records/
```

Step 11.
Colect static files, collects all static files to media, collectstatic and static folders.
```
python manage.py collectstatic
```

Step 12.
Restart Apache server, do it everytime after changes been made to the site.
```
service apache2 restart
```

Before deployment, Do not forget to change settings.py
ALLOWED_HOSTS = [] should hold ip address, domain name, star means all hosts are allowed.
```
DEBUG = True

ALLOWED_HOSTS = ['*']



STATIC_URL = '/static/'
              
STATIC_ROOT = '/var/www/venv/web_app_may_8/blog_project/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/var/www/venv/web_app_may_8/blog_project/staticfiles/')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/var/www/venv/web_app_may_8/blog_project/media/')
```


