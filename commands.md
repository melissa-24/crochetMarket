# Commands:

## Working with an Environment

### Create new:
python3 -m venv projectNamePy3Env

### Activate environment
* Windows:
    source projectNamePy3Env/Scripts/activate
* Mac:
    source projectNamePy3Env/bin/activate

### Package installs:
pip install packageName

### Updating a package:
pip install --upgrade packageName

### Shutting down environment:
**** This can be done regardless of folder you are in
deactivate

## Creating Django Project & App
Make sure you are where you want your project to be before continuing on

### Step 1:
Activate environment with Django installed

### Step 2:
django-admin startproject projectName

### Step 3:
Test it installed by running the following command (after moving into the project folder that was just created)

python3 manage.py runserver

You will see notations about migrations don't worry about this yes

In a browser navigate to localhost:8000

ctrl + c shuts the server down

### Step 4:
Create 1st application

python3 manage.py startapp projectApp

## Now what?

Those are the basic steps to get things started after this is up to you and what you want to create