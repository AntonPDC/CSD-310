import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime


def fetch_and_display_data(cursor, query, title):
    """Fetch data using the provided query and display with formatted dates."""
    cursor.execute(query)
    results = cursor.fetchall()

    print(f"\n-- {title} --")
    for row in results:
        formatted_row = [
            col.strftime("%Y-%m-%d") if isinstance(col, date) else col for col in row
        ]
        print(formatted_row)


def main():
    config = {
        "user": "local_user",
        "password": "secure_password",
        "host": "127.0.0.1",
        "database": "willson_financial",
        "raise_on_warnings": True,
    }

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Query to fetch data
        query_clients = "SELECT Client_ID, First_name, Last_name, Email, Phone FROM Client"
        query_accounts = "SELECT Account_ID, Account_type, Balance, Open_Date FROM Account"

        # Fetch and display client data
        fetch_and_display_data(cursor, query_clients, "Client Data")

        # Fetch and display account data with formatted dates
        fetch_and_display_data(cursor, query_accounts, "Account Data")

        db.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()


if __name__ == "__main__":
    main()
