# movie_rating
django application for movie ratings and swagger integration

# initial setup
- clone the repo
- create virtual env: ```python3 -m venv .venv```
- activate virtual env: ```source .venv/bin/activate```
- run: ```pip install -r requirement.txt```
- to start the server: ```python manage.py runserver```
- visit: http://127.0.0.1:8000/doc/


# sample data
- db.sqlite3 contains sample data
- if you want to start fresh
  - delete db.sqlite3
  - delete all migrations
  - comment rating.urls file content, so that import wont interfere in our migrations
  - do: ```python manage.py makemigrations```
  - do: ```python manage.py migrate```
  - uncommnet rating.urls file content
  - uncomment function ```create_movie_entries()``` from rating.urls.py if you want to use data.py
  - Note: after running once, uncomment above function so data would be created multiple times

# APIs

API to submit ratings (between 1-10) by users for a selected movie.
- POST http://127.0.0.1:8000/rating/give_rating_by_name/{movie_title}/{username}/{rating}
- POST http://127.0.0.1:8000/rating/give_rating_by_id/{movie_id}/{user_id}/{rating}

API to get the rating (between 1-10) of a selected movie.
- GET http://127.0.0.1:8000/rating/getMovieRatingByName/{movie_title}
- GET http://127.0.0.1:8000/rating/getMovieRatingById/{movie_id}

API integration for fetching pincodes.
- GET http://127.0.0.1:8000/rating/postoffice/PINCODE

API to search for list of active movies in a pincode.
- GET http://127.0.0.1:8000/rating/active_movies/110001

# UNIT TEST CASE
- to run them: ```python manage.py test tests```