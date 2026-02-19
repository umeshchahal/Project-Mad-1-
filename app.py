from flask import Flask 
from application.database import db # database
app = None 

def create_app():
     app = Flask(__name__ )
     app.debug = True 
     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecard.sqlite3" # database
     db.init_app(app) # database 

     app.app_context().push() # runetime error , brings everything undercontext of flask application 
     return app 
     
     # with app.app_context():
     #    db.create_all()

     # return app
app = create_app() 
from application.controllers import * # 2 controllers


if __name__ == "__main__":
     app.run()

