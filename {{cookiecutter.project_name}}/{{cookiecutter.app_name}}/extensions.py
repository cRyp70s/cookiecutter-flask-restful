"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
{%- if cookiecutter.use_request_limiter == "yes" %}
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from {{cookiecutter.app_name}}.config import RATE_LIMIT
{%- endif %}

{%- if cookiecutter.use_celery == "yes" %}
from celery import Celery
{%- endif %}

from {{cookiecutter.app_name}}.commons.apispec import APISpecExt


db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
apispec = APISpecExt()
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
{%- if cookiecutter.use_celery == "yes" %}
celery = Celery()
{%- endif %}

{%- if cookiecutter.use_request_limiter == "yes" %}
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=RATE_LIMIT
)
{%- endif %}
