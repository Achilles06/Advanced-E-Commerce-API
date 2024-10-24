import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('postgresql://toji_ct_end_project_user:Nvn0IQ6MQZ0i3yUTGslRMLbcth9p0DTx@dpg-csdco4jqf0us73b3fkqg-a.oregon-postgres.render.com/toji_ct_end_project','postgresql://33toji:Nvn0IQ6MQZ0i3yUTGslRMLbcth9p0DTx@dpg-csdco4jqf0us73b3fkqg-a:5432/toji_ct_end_project')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    RATELIMIT_DEFAULT = "100 per day"
