#!/bin/bash
rm -f db.sqlite3
rm -rf TripShare/migrations
python manage.py makemigrations TripShare
python manage.py makemigrations
python manage.py migrate
python populate_trip.py
