
import os

class Config:
    """
    Application configuration class.
    Loads settings from environment variables.
    """
    # Secret key for signing session cookies and other security purposes.
    # It's crucial this is kept secret.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLAlchemy database URI. Specifies the database engine and connection details.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # Disable SQLAlchemy's event system to save resources if not needed.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Better performance for SQLAlchemy Engine.
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,
        'pool_pre_ping': True
    }
