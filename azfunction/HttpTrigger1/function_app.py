import azure.functions as func
from __init__ import app as flask_app  # Import Flask app from __init__.py

# The main function to handle requests and forward to Flask
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Azure function wrapper for the Flask application."""
    return func.WsgiMiddleware(flask_app.wsgi_app).handle(req, context)
