from flask import Flask
from config import Config
from models import db
from routes import register_all_routes
from utils.cache import init_cache
from utils.jwt_auth import init_jwt
from utils.limiter import init_limiter

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
init_cache(app)
init_jwt(app)
init_limiter(app)

# Register all routes
register_all_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
