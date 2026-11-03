from flask import Flask

def create_app():
    """
    Función factory que crea y configura la aplicacion Flask.
    """
    app = Flask(__name__)

    # Importamos y registramos los blueprints (rutas)
    # Blueprints allow us to organize our application into modules, making it easier to manage and scale. 
    # Each blueprint can have its own routes, templates, and static files. In this case, we have three blueprints: 
    # users_bp for user-related routes, cars_bp for car-related routes, and rentals_bp for rental-related routes. 
    # By registering these blueprints with the Flask app, we integrate their routes into the main application.
    from app.routes.users import users_bp
    from app.routes.cars import cars_bp
    from app.routes.rentals import rentals_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(cars_bp)
    app.register_blueprint(rentals_bp)

    return app