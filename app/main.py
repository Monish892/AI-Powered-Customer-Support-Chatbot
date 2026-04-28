
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This should be done before importing the app and config
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app

# Create the Flask app instance using the app factory
app = create_app()

if __name__ == '__main__':
    # The application is run via the Flask CLI or a production server like Gunicorn.
    # This 'if' block allows direct execution for simple development environments.
    # Debug mode is controlled by the FLASK_ENV environment variable.
    app.run(host='0.0.0.0', port=5000)
