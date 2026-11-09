from app import create_app

app = create_app() # Here we are creating the application instance by calling the create_app function defined in the app/__init__.py file. This function sets up the Flask application, registers blueprints, and configures any necessary settings. The resulting app object is an instance of the Flask class, which will be used to run the web server and handle incoming requests.

if __name__ == "__main__":
    app.run(debug=True) # The app.run(debug=True) line starts the Flask development server. The debug=True argument enables debug mode, which provides detailed error messages and automatically reloads the server when code changes are detected. This is useful during development, but it should be turned off in a production environment for security reasons.