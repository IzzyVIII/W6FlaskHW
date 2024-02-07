from flask import Flask
from flask_migrate import Migrate 

# internal imports
from config import Config
from .models import login_manager, db
from .blueprints.site.routes import site
from .blueprints.auth.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

# wrap our whole app in our login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_id' #authentication route 
login_manager.login_message = 'Hey there! Please Login' 
login_manager.login_message_category = 'warning'


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
app.register_blueprint(site)
app.register_blueprint(auth)

# intantiate our database & wrap our app in it
db.init_app(app)
migrate = Migrate(app, db) #things we are connecting/migrating (our application to our database)