"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

{%- if cookiecutter.use_celery == "yes" %}
CELERY = {
    "broker_url": os.getenv("CELERY_BROKER_URL"),
    "result_backend": os.getenv("CELERY_RESULT_BACKEND_URL"),
}
{%- endif %}

{%- if cookiecutter.use_request_limiter == "yes" %}
RATE_LIMIT = ["10 per second", "50 per minute"]
{%- endif %}
