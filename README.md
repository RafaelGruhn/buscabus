# Pegabus


## Starting Local

`docker-compose up --build`

*Default Address:* `0.0.0.0:8080`

## Create admin user

`docker exec -it <container name> /bin/bash`
`python manage.py createsuperuser`

## Clear local database

`docker-compose down -v`
