# command to run the this app
STEPS:
  1. first add env file or set environment variable
  2. install docker and docker-compose in your system
  3. run this project via docker compose > docker-compose up --build
  4. open another terminal makemigratation and migrate all table in database
  5. command >  docker-compose exec django-app python3 manage.py makemigrations && python3 manage.py migrate

      
