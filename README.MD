#  Reservation Application
Before running the app, you need to install all the dependencies.

## Installing a virtual environment and all the dependencies and packages

### Install a virtual environment

Create a virtual environment to install dependencies:

`python3 -m venv ./.virtualenvs/reservations`

and activate the virtual environment **reservations** with the following command:

`source .virtualenvs/reservations/bin/activate`

### Install Django or install all the dependencies

Run the following command in the virtual environment environment if the app is created for the first time to install **django**:

`pip install django`

or if the application is downloaded from GIT, then install the dependencies:

`pip install -r requirements.txt`

## Apply migrations

If database is going to be created for the first time run a migration

`python3 manage.py migrate`

If the database has new models and or a model changed run the makemigration tool:

`python3 manage.py makemigrations`

## Create Super user only for the first time

To create a super user for administration, run the following command:

`python manage.py createsuperuser`