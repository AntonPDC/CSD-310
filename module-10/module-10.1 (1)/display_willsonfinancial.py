import mysql.connector
from mysql.connector import errorcode
from datetime import date
from decimal import Decimal

# Configuration for the database connection
config = {
    'user': 'Willson_user',
    'password': 'securepassword123',
    'host': '127.0.0.1',
    'database': 'WillsonFinancial',
    'raise_on_warnings': True
}

try:
    # Connect to the database
    db = mysql.connector.connect(**config)
    print("\n Database user '{}' connected to MySQL on host '{}' with database '{}'".format(
        config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()
    tables = ["Clients", "Accounts", "Assets", "Transactions", "Employees", "Compliance", "Billing"]

    # Iterate through each table and display data
    for table in tables:
        print(f"\n--- Data from {table} ---")
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        
        # Format datetime.date and Decimal for cleaner display
        for row in rows:
            formatted_row = tuple(
                str(item) if isinstance(item, date) else
                float(item) if isinstance(item, Decimal) else
                item
                for item in row
            )
            print(formatted_row)
        
        if not rows:
            print(f"No data available in {table}.")
    
    input("\n\n Press any key to exit...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("* The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("* The specified database does not exist")
    else:
        print(err)
finally:
    try:
        db.close()
        print("\nConnection closed.")
    except NameError:
        print("\nConnection was never established.")
