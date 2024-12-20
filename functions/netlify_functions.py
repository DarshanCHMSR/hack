from flask import Flask
from werkzeug.wrappers import Request, Response
from app import app  # Import your Flask app

def handler(event, context):
    """
    AWS Lambda function handler for Netlify
    """
    # Convert event to WSGI environment
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.serving import run_simple

    def simple_app(environ, start_response):
        # Run the app
        return app(environ, start_response)

    wsgi_app = DispatcherMiddleware(simple_app)
    request = Request(event)
    response = Response=()
