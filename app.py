from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from models import db, Task
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Necessary for CSRF protection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
#from routes import *
if __name__ == '__main__':
    app.run(debug=True)
