# Houses Application

I am learning to create Houses App using Python Django, and ReactJS

> 1. <https://www.cloudamqp.com/>
> 1. <http://localhost:3000/config/houses>

## Creating Admin User

```powershell
docker network create housesappnetwork

# python manage.py createsuperuser
Username (leave blank to use 'root'): admin@example.com
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.

mysql -u microservice -p core
show tables;
```

## Backend - Config

> 1. To be done

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python.exe -m pip install --upgrade pip

pip install django
pip install djangorestframework
pip install flask

django-admin startproject config
python manage.py runserver

python manage.py migrate

pip install mysqlclient
pip install pika
pip install django-mysql
pip install django-cors-headers

pip freeze > .\requirements.txt
pip install –r requirements.txt

docker build --pull --rm -f "Dockerfile" -t housesservices:latest -t vishipayyallore/housesservices:latest .
```

## Backend - Houses App

```powershell
docker-compose exec backend sh

django-admin startapp houses

python manage.py makemigrations

python manage.py migrate
```

![Make Migrations](documentation/images/Make_Migrations.PNG)

![Create Super User](documentation/images/CreateSuperUser.PNG)

![Admin Site](documentation/images/Admin_Site.PNG)

## Backend - Core Services

```powershell
pip install Flask Flask-SQLAlchemy SQLAlchemy Flask-Migrate Flask-Script Flask-Cors
pip install requests mysqlclient markupsafe itsdangerous jinja2 werkzeug pika pytz

docker build --pull --rm -f "Dockerfile" -t coreservices:latest -t vishipayyallore/coreservices:latest .

docker-compose exec backend sh

rm -rf migrations
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
flask db downgrade
```

## Frontend

> 1. To be done

```powershell
npx create-react-app housesweb --template typescript
```

## Appendix A

```python
# config/settings.py
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

curl -v http://housesservices-backend-1:8000/api/houses
curl -v http://localhost:8000/api/houses
curl -v http://housesservices-backend-1:8000/api/checker

```
# Access MySQL client
mysql -u your_username -p your_database_name
Enter password: ********

# Inside MySQL client
mysql> SELECT * FROM alembic_version;
+----------------+-------------+
| version_num    | timestamp   |
+----------------+-------------+
| 9d599c0c6ccf   | 2024-01-01  |
+----------------+-------------+

# If there are entries, delete them
mysql> DELETE FROM alembic_version;

# Verify the table is empty
mysql> SELECT * FROM alembic_version;
Empty set (0.00 sec)

# Exit the MySQL client
mysql> exit;
Bye
```

## Reference(s)

> 1. <https://learn.microsoft.com/en-gb/dotnet/aspire/get-started/build-your-first-aspire-app?pivots=visual-studio>
> 1. <https://learn.microsoft.com/en-gb/dotnet/aspire/deployment/azure/aca-deployment>
> 1. <https://learn.microsoft.com/en-gb/dotnet/aspire/fundamentals/telemetry#export-opentelemetry-data-for-monitoring>
> 1. <https://learn.microsoft.com/en-gb/dotnet/aspire/deployment/azure/application-insights>
> 1. <https://learn.microsoft.com/en-gb/training/modules/use-telemetry-dotnet-aspire/6-exercise-use-telemetry-dotnet-aspire>
> 1. <https://devblogs.microsoft.com/dotnet/introducing-aspnetcore-metrics-and-grafana-dashboards-in-dotnet-8/>
> 1. <https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire-simplifying-cloud-native-development-with-dotnet-8/>
