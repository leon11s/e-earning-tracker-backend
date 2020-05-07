# IoT platforma - backend

## Docker
- Run:
    - `docker-compose up --build -d`

- Test:
    - `docker-compose exec iot-backend pytest .`

## Dev
- Enter database
    - `docker-compose exec db psql --username=elearn --dbname=elearntracking`
