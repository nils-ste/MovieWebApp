from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie, User
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
    user = data_manager.create_user(request.form['name'])
    return redirect(url_for('index'))

@app.route('/users/<int:user_id>/movies', methods=['GET'])
def list_movies(user_id):
    movies = data_manager.get_movies(user_id)
    user = User.query.get_or_404(user_id)
    return render_template("favorite_movies.html", user_id=user_id, movies=movies, user=user)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def new_movie(user_id):
    title = request.form['title']
    data_manager.add_movie(user_id, title)
    return redirect(url_for('list_movies', user_id=user_id))

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