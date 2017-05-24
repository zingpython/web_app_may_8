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