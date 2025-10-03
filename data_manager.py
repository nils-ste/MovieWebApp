from models import db, User, Movie
import requests

api_url = "http://www.omdbapi.com/?apikey=841017c3"

class DataManager():
    # Define Crud operations as methods
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
    def get_users(self):
        return User.query.all()
    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()
    def add_movie(self, movie, user_id):
        try:
            url = f"{api_url}&t={title}"
            response = requests.get(url)
            if response.status_code != 200:
                return
            data = response.json()

            year = int(data.get("Year", 0) or 0)
            rating_str = data.get("imdbRating") or "0"
            rating = float(rating_str)  # your model uses Integer

            poster = data.get("Poster") or ""
            director = data.get("Director") or ""

            new_movie = Movie(
                title=title,
                year=year,
                director=director,
                poster_url=poster,
                rating=rating,
                user_id=user_id,
            )
            db.session.add(new_movie)
            db.session.commit()
        except Exception as e:
            print("We can't find this movie in the imDB Database, please try again later")

    def update_movie(self, movie_id, new_title):
        pass
    def delete_movie(self, movie_id):
        pass


