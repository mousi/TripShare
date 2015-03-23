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
pip install -r requirements.txt
```
It will install all the necessary packages in order to use this application.

Now, you need to setup the database for the application. There is a script ready to create the database and populate it.
In your terminal, enter:
```
./update_db.sh
```

Finally, enter the following to your terminal:
```
python manage.py runserver
```

Enjoy!!!