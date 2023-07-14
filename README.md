# Setup

Create a `.env` file with the following variables:
```
FLASK_SECRET_KEY = <secret key>
FLASK_SQLALCHEMY_DATABASE_URI = <database URI>
```

Create the database:
```
docker compose exec app flask create_db
```

# Run the project
```
docker compose up --build -d
```

http://localhost:8000/