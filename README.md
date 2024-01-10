# django_smartnotes

This repository adds another CRUD app to the sea of sad CRUD apps. It is written in *Python* using the **Django** framework to set the first stepping stone into the Django world.

Created by Atilay Tamkan <tamkan.atilay@gmail.com>

## Features

- User-specific posts: After authentication, users can see their posts in order and edit or delete them if they wish.

## Setup

Please make sure that you have [Python](https://www.python.org/downloads/) Version >= 3.8.

- Clone this repository to your local machine using ```git clone https://github.com/atilayyuri/django_smartnotes.git```

- Setup the environment by executing below in order (to activate venv on Windows, use ```.\venv\Scripts\Activate.ps1```, for PowerShell or ```.\venv\Scripts\activate.bat``` for cmd. Use ```Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force``` if you got authorization errors)
```
cd django_smartnotes
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r ./smartnotes/requirements.txt
``` 

## Execution
```
python3 manage.py runserver 127.0.0.1:8732
```
Visit the web browser with 'https://127.0.0.1:8732' 

Sign up with a username and password to use the app. 

    


