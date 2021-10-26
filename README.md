## Getting started
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.6 and above](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)


## Installing
### Setting up the database
- Start your database server and create your database

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/nicksonlangat/energy_consumption.git) `git clone https://github.com/nicksonlangat/energy_consumption.git`
- Navigate to the project directory
- Create a virtual environment `python3 -m venv name_of_your_virtual_environment` and activate it `source name_of_your_virtual_environment/bin/activate`
- Create a .env file next to `settings.py` and put these key=values in it:
```
DEBUG=on
SECRET_KEY='your secret key'
DB_NAME="your_db_name"
DB_USER="your_postgres_username"
DB_PASS="your_postgres_password"
DB_HOST="localhost or any other host name"
```
- Install dependencies to your virtual environment `pip install -r requirements.txt`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## PROJECT MODULES
- The project configs and settings is in the folder `mysite`
- The main app is in the folder  `core`
- I added an optional app `accounts` for auth purposes. It uses a custom user model.

## FEATURES
- Pagination on the buildings list to display 10 items per page
- Data visualisation using  [Chart Js](https://www.chartjs.org/)
- Unit tests to try and catch bugs early on. Run `python manage.py test` to have a go

## CONTAINERISATION
- Used Docker 
- You can build the spin up the docker containers by `docker-compose -f docker-compose.yml up --build `
- Visit `localhost` to view the app running inside the container. 

## DEPLOYMENT
- Hosted it on AWS using ECS
- To deploy create an ecs context using docker then run the compose application on Amazon ECS.
- Check my sample here `http://ec2-18-191-244-15.us-east-2.compute.amazonaws.com/`



