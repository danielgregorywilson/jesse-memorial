# lcog-hr

# Setting up for the first time
Create a copy of mainsite/settings_local.py.example (remove the '.example')
## Set up a Postgres server locally
-Download Postgres and pgAdmin apps
-Follow these steps: https://djangocentral.com/using-postgresql-with-django/
    -Create a database called 'hr_app'
    -Create a DB user for the DB
    -Set defaults for user (e.g. utf-8) and grant DB permissions to user
-Set DB name, username, and password in settings_local
## Set up Python/Django environment
Create a Python virtualenv in the parent directory of the source controlled code
`virtualenv env_20210302` (the date)
Create a symlink to the dated virtualenv
`ln -s env_20210302 env`
Activate the virtual environment
`source env/bin/activate` 
Install requirements (pip version pip 20.1.1 (python 3.8))
`pip install -r code/requirements.txt`
Run Django migrations
`./manage.py migrate`
Create a superuser to log in to backend
`./manage.py createsuperuser`
## Set up Quasar frontend
`cd frontend`
`npm install`


# Run the backend locally
Activate the virtual environment
`source env/bin/activate` 
Start the server
`./manage.py runserver`

# Run the frontend locally
`cd frontend`
`quasar dev`

# Deploy backend
In mainsite/middleware/CorsMiddleware, make sure the correct response["Access-Control-Allow-Origin"] is commented out.
`eb deploy --profile lcog`

# Deploy frontend
`cd frontend`
`quasar build`
Navigate to https://s3.console.aws.amazon.com/s3/buckets/lcog-hr-frontend/
Under the 'Objects' tab is the list of files
Drag the contents of frontend/dist/spa to the window to upload the build

# Testing
Run frontend end-to-end tests
`npm run cypress:open`

# Production Sites
Production Frontend - http://lcog-hr-frontend.s3-website-us-west-2.amazonaws.com
Production API - http://lcog-internal-env.eba-4t9yrmiu.us-west-2.elasticbeanstalk.com/api/
Production Backend - http://lcog-internal-env.eba-4t9yrmiu.us-west-2.elasticbeanstalk.com/admin/