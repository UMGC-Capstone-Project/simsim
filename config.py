import os

def get_env_or_default(key, defaultValue):
    value = os.getenv(key)
    if value == None:
        return defaultValue
    return value

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY: str = get_env_or_default('APP_SECRET_KEY','cnG*DS8@wFZNly95F5d#')
    SQLALCHEMY_DATABASE_URI = get_env_or_default('APP_DATABASE_URI','sqlite:///users.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env_or_default('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    PORT = os.getenv('APP_PORT')

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True

class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False