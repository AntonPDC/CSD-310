import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True,
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
# Query for all fields in studio
    query_studio = "SELECT * FROM studio"
    cursor.execute(query_studio)
    studio_results = cursor.fetchall()
    print("\n Studio results: {}".format(studio_results))
# Query for all fields in genre
    query_genre = "SELECT * FROM genre"
    cursor.execute(query_genre)
    genre_results = cursor.fetchall()
    print("\n Genre results: {}".format(genre_results))
# Query short movies
    query_short_movie= "SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120"
    cursor.execute(query_short_movie)
    short_movie_results = cursor.fetchall()
    print("\n Short Movie results: {}".format(short_movie_results))
# Query movies grouped by director
    query_by_director= "SELECT film_director, film_name FROM film ORDER BY film_director, film_name"
    cursor.execute(query_by_director)
    director_results = cursor.fetchall()
    print("\n Director results: {}".format(director_results))




    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The database '{}' does not exist.")
    else:
        print(err)
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nDatabase connection closed.")