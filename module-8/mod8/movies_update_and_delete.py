import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True,
}


def show_films(cursor, title):

    query = '''
        SELECT 
            film.film_name AS Name, 
            film.film_director AS Director, 
            genre.genre_name AS Genre, 
            studio.studio_name AS `Studio Name`
        FROM 
            film
        INNER JOIN 
            genre ON film.genre_id = genre.genre_id
        INNER JOIN 
            studio ON film.studio_id = studio.studio_id
    '''

    try:
        cursor.execute(query)
        films = cursor.fetchall()

        print("\n  -- {} --  ".format(title))

        for film in films:
            print(
                "Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    except Exception as e:
        print(f"An error occurred: {e}")

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    show_films(cursor, "DISPLAYING FILMS")


    print("\nInserting a new horror film 'The Omen'...")
    insert_film = '''
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime, film_releaseDate)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_film, ("The Omen", "Richard Donner", 2, 1, 111, "1976"))  # Genre ID 2 for Horror
    db.commit()
    show_films(cursor, "AFTER INSERTING 'THE OMEN'")
#UPDATE
    print("\nUpdating the film 'Alien' to genre Horror...")
    update_film = '''
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien'
    '''
    cursor.execute(update_film)
    db.commit()
    show_films(cursor, "AFTER UPDATING 'ALIEN' TO HORROR GENRE")

# DELETE
    delete_film = '''
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    '''
    cursor.execute(delete_film)
    db.commit()
    show_films(cursor, "AFTER DELETING 'GLADIATOR'")

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

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