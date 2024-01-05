import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app
connex_app.app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'authors.db'}"
connex_app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(connex_app.app)
ma = Marshmallow(connex_app.app)