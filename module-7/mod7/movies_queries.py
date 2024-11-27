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
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studio_results:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()
# Query for all fields in genre
    query_genre = "SELECT * FROM genre"
    cursor.execute(query_genre)
    genre_results = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genre_results:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre: {genre[1]}")
        print()
# Query short movies
    query_short_movie= "SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120"
    cursor.execute(query_short_movie)
    short_movie_results = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for name, runtime in short_movie_results:
        print(f"Film Name: {name}")
        print(f"Film Runtime: {runtime}")
        print()
# Query movies grouped by director
    query_by_director= "SELECT film_director, film_name FROM film ORDER BY film_director, film_name"
    cursor.execute(query_by_director)
    director_results = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for director, name in director_results:
        print(f"Director: {director}")
        print(f"Film Name: {name}")
        print()

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