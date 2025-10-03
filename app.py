from flask import Flask, render_template
from data_manager import DataManager
from models import db, Movie
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager()  # Create an object of your DataManager class


@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)

@app.route('/users')
def list_users():
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string

@app.route('/users', methods=['POST'])
def new_user():
    pass

@app.route('/users/<int:user_id>/movies', methods=['GET'])
def list_movies(user_id):
    pass

@app.route('/users/<int:user_id>/movies', methods=['POST'])
def new_movie(user_id):
    pass

@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id,movie_id):
    pass

@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id,movie_id):
    pass




if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run()