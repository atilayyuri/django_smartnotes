# django_smartnotes

This repository adds another CRUD app to the sea of sad CRUD apps. It is written in *Python* using **django** framework with the intention to set the first stepping stone into django world.

Created by Atilay Tamkan <tamkan.atilay@gmail.com>

## Features

- User-specific posts: After authentication, the user can see their posts in order, and edit or delete them if they wish.

## Setup

Ensure that you have [Python](https://www.python.org/downloads/) Version >= 3.8.

- Clone this repository to your local machine using ```git clone https://github.com/atilayyuri/django_smartnotes.git```

- Setup the environment by executing below in order (to activate venv on Windows use ```.\venv\Scripts\Activate.ps1```, make sure you are using cmd instead of PowerShell and use ```Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force``` if you got authorization errors)
```
cd django_smartnotes
python -m venv venv
source .venv/bin/activate
python -m pip install -r ./smartnotes/requirements.txt
``` 

## Execution
```
python manage.py runserver 127.0.0.1:8732
```
Visit the web browser with 'https://127.0.0.1:8732' 

Sign up with username and password to use the app. 

    


