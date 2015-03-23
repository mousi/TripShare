# TripShare
TripShare is a team project for ITECH 2015.

Clone the application to your machine:
```
git clone https://github.com/liverpoolaras/TripShareProject.git
```

To install it to your machine, first create a virtual environment <name>. 
```
mkvirtualenv <name>
```

When the environment is created, go to the application's folder in your machine and enter:
```
pip install -U -r requirements.txt
```
It will install all the necessary packages in order to use this application.

Now, you need to setup the database for the application. 
<ol>
<li>If you work on Windows, you need to enter the following:</li>
  <ol>
    <li><i>python manage.py makemigrations TripShare</i></li>
    <li><i>python manage.py migrate</i></li>
    <li><i>python populate_trip.py</i></li>
  </ol>
  
  <li>If you work in a UNIX based machine, there is a script ready to create the database and populate it.
In your terminal, enter: <i>./update_db.sh </i></li>
</ol>

If you want to create an admin enter the following:
```
python manage.py createsuperuser
```
and follow the instructions.

Finally, enter the following to your terminal:
```
python manage.py runserver
```

Enjoy!!!
