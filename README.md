# SP23-ADT-Final-Project
## Student Management System

To activate the virtual environment
```
source /Users/pkamburu/SP24-ADT-Final-Project/env/bin/activate
```

To run the project
```
python manage.py runserver
```

or you can run the project from here.
```
python manage.py runserver 8809
```


To add the project,
```
python manage.py startapp project
```

If you create a new app, please add it in the INSTALLED_APPS=[ ] in settings.py file. 
like this, 
```
project_name
```

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
python manage.py migrate
```
It's not handle the URL redirection yet. So need to specify which url you are reffering first. 

