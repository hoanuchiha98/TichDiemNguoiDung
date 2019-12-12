from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from database.db_connections import POSTGRES_CONNECTION_STR
from swagger_config import connex_app

flask_app = connex_app.app

flask_app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_CONNECTION_STR
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
flask_app.config["SQLALCHEMY_ECHO"] = True  # turn on sql query on logging
flask_app.config["CORS_HEADERS"] = 'Content-Type'
flask_app.config['SECRET_KEY'] = "QdjqxOEiclZ5OIM26yBxd6K5N4TgsW3UYNG0uc5hvn0IGrbgTeSW52wld0svkUjABJJ5rUL5VBSMGOpHpswhUqjJhaRR7W2MKyC1E4bvs8dE0Ft1dRlckaacpWZ9oBIuXPLYUZVeqpOMwR3dWr4SLkwt142hsSZxwR3dWr4SLkwt142hsSZx4bN8mIifIh7Uh0tGHk59"

db = SQLAlchemy(flask_app)
ma = Marshmallow(flask_app)
CORS(flask_app, resources={r"/api/*": {"origins": "*"}})