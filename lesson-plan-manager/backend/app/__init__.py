from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from app.config.settings import Config
from app.database.db import db
from app.models.lesson_plan import LessonPlan
from app.routes.lesson_plan_routes import (
    lesson_plan_bp
)

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    Swagger(app)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(lesson_plan_bp)

    @app.route("/")
    def home():

        return {
            "message": "API is running"
        }
        
    @app.route("/health")
    def health():
        return {
            "status": "healthy"
        }

    return app