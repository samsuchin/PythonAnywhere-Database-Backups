#!/usr/bin/python3.8

import os
import datetime

DJANGO_ROOT = "" #Folder location of manage.py. Should look like: "/home/myusername/myproject/"
DAYS_TO_KEEP_BACKUP = 3 #Backups past this amount are deleted.
BACKUP_NAME_SUFFIX = "backup.json" #Suffix name and extension. Example result: 06-06-2020_backup.json
BACKUP_FOLDER_NAME = "fixtures" #Name of folder in Django Root to store backups.

"""
^^^^^^^^^^^^^^^^^ Edit These Variables ^^^^^^^^^^^^^^^^^
"""

os.chdir(r"{}".format(DJANGO_ROOT))
now = datetime.datetime.now().strftime("%m-%d-%Y")


days_ago = (datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_BACKUP)).strftime("%m-%d-%Y")

try:
    os.remove("fixtures/{}_{}".format(days_ago, BACKUP_NAME_SUFFIX))
    os.system("echo Removed file {}_{}".format(days_ago, BACKUP_NAME_SUFFIX))
except:
    os.system("echo File {}_{} not removed. It may not exist.".format(days_ago, BACKUP_NAME_SUFFIX))

os.system("python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 2 > {}/{}_{}".format(BACKUP_FOLDER_NAME, now, BACKUP_NAME_SUFFIX))