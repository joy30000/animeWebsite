# from flask import Flask,Blueprint
# app=Flask(__name__)

# @app.route('/')
# def hellworld():
#   return'hello world'

# if __name__=="__main__":
#   app.run(debug=True)
# app.py




# from flask import Flask,redirect, url_for
# from routes import homeRoutes  # Import homeRoutes from the routes folder


# # Create the Flask app
# app = Flask(__name__)

# # Register the Blueprint with a URL prefix
# app.register_blueprint(homeRoutes, url_prefix='/home')
# # Route for the root path to redirect to /home
# @app.route('/')
# def redirect_to_home():
#     return "welcome"  # Redirects to /home/

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, redirect, url_for,send_from_directory
from flask_cors import CORS
from routes import homeRoutes  # Import homeRoutes from the routes folder
import os

# Create the Flask app
#app = Flask(__name__)
app = Flask(__name__)
CORS(app)

# Register the Blueprint with a URL prefix
app.register_blueprint(homeRoutes, url_prefix='/home')

# Route for the root path to redirect to /home
@app.route('/')
# def serve_react():
#     return send_from_directory(os.path.join(app.static_folder, 'index.html'))
def redirect_to_home():
    return "welcome"  # Redirects to /home/

# Run the Flask app on the appropriate host and port
if __name__ == "__main__":
    # Get the port from the environment variable (for cloud deployment)
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if not provided
    app.run(host='0.0.0.0', port=port, debug=True)  # Use 0.0.0.0 to listen on all interfaces