# PythonAnywhere-Django-Database-Backups
Customizable Python script to simultaneously backup Django databses and delete old ones after a certain time frame on PythonAnywhere's scheduled tasks. This script uses Django's dumpdata and excludes contenttypes and auth.permission. I found dumpdata to be friendlier than mysqldump. After dumpdata, one can simply loaddata to fill in the database.
https://docs.djangoproject.com/en/3.0/ref/django-admin/


## Why should I use this?

The importance of backing up your website database is given. This script allows one to not only save daily backups of their Django site but to also automatically delete old backups to save storage. I use this script for all of my websites and wish I had it when I started web dev.

## How to use

Save this file as backup.py in your Django Root folder where manage.py is located on PythonAnywhere.

Create a back up folder in your Django Root to store the backups. fixtures/ is commonly used.

Open the backup.py file, and then edit the top variables to work with your website. Also, change the python version at the very top of the file to match yours.

Then navigate to Tasks on PythonAnywhere. Enter...<br/>
**source virtualenvwrapper.sh && workon (YOUR VENV NAME) && (YOUR PYTHON VERSION) /home/(PYTHONANYWHERE USERNAME)/(DJANGO_ROOT_FOLDER)/backup.py**

With this template, yours could look like...<br/>
**source virtualenvwrapper.sh && workon venv && python3.8 /home/samsuchin/mysite/backup.py**

Enter the frequency and time to run the script, and then finally create it.
