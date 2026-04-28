
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .aiml_kernel import AimlKernel

# Initialize extensions, but don't configure them yet
db = SQLAlchemy()

# Initialize the AIML Kernel a single time for the application
# This is more efficient as it avoids reloading the AIML files on every request.
base_dir = os.path.abspath(os.path.dirname(__file__))
aiml_path = os.path.join(base_dir, '..', 'aiml_set')
aiml_kernel = AimlKernel(aiml_path=aiml_path)

def create_app(config_class=Config):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration from the 'config_class' object
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)

    # The application context is necessary for database operations
    with app.app_context():
        # Register Blueprints for organizing routes
        from . import routes
        app.register_blueprint(routes.main_bp)

        # You might want to create tables if they don't exist.
        # In a production setup, this is typically handled by migration tools
        # like Alembic. For this project, we assume manual setup via schema.sql.
        # db.create_all() 

    return app
