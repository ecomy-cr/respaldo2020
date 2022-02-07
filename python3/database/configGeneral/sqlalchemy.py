from flask import Flask

import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/pruebaDBsqlite3.db"
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='azbadsasdsdasf4r54qw5ty',DATABASE=os.path.join(app.instance_path, 'pruebaDB2.sqlite3'),)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAX_CONTENT_LENGTH"] = 16*2**20
app.config["ALLOWED_EXTENSIONS"] = set(["pdf","png","jpg","jpeg"])
app.config["SESSION_TYPE"]="filesystem"
app.config["SESSION_FILE_DIR"]=os.path.join(app.root_path, "cache")
#app.config["SECRET_KEY"]= "azbadsasdsdasf4r54qw5ty"
app.config["SESSION_FILE_THRESHOLD"]= 1000
Base = declarative_base()
engine = create_engine(dbdir)
session_maker = sessionmaker()
session_maker.configure(bind=engine)
Base.metadata.create_all(engine)

sessionx = session_maker()

db = SQLAlchemy(app)

#app.secret_key =  'azby'

try:


    class UsuariosOficiales(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(80), nullable=False)
        
        def serialize (self):
            return {
            "id": self.id, "username" : self.username
            }

    db.create_all()
    db.session.commit()

except Exception as e:
    print(str(e))


def create_app():
    
    @app.route("/")
    def home():
        pass

    @app.route("/loginf", methods=["GET", "POST"])
    def loginf():
        if request.method == "POST":
            pass

    return app
