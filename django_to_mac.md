
# Start using Virtual Environment and Django on Mac

    1. Open Terminal (Applications > Utilities > Terminal)

    2. Enter the following commands: The command sudo will require an admin password. The same password you use to install other programs. 

    3. Install Pip. (Python Package Installer):


```python
sudo easy_install pip
```

    4. Install virtualenv:


```python
sudo pip install virtualenv
or if you get an error
sudo -H pip install virtualenv
```

    5. Navigate to where you want to store your code.


```python
mkdir my_django_project
cd my_django_project
```

    6. INSIDE my_django_project folder create a new virtualenv:


```python
virtualenv env
```



    7. Activate virtualenv:



```python
source env/bin/activate
```



The result in Terminal should be like:



```python
(env)Name_of_your_computer:my_django_project name_of_your_computer$
```

    8. Install Django:


```python
pip install django
```







