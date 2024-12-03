# from flask import Flask,Blueprint
# app=Flask(__name__)

# @app.route('/')
# def hellworld():
#   return'hello world'

# if __name__=="__main__":
#   app.run(debug=True)
# app.py
from flask import Flask
from routes import homeRoutes  # Import homeRoutes from the routes folder

# Create the Flask app
app = Flask(__name__)

# Register the Blueprint with a URL prefix
app.register_blueprint(homeRoutes, url_prefix='/home')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)