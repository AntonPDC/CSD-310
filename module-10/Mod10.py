import mysql.connector
from mysql.connector import errorcode

# MySQL database configuration
config = {
    "user": "your_user",
    "password": "your_password",
    "host": "127.0.0.1",
    "database": "willson_financial",
    "raise_on_warnings": True,
}

# Function to execute SQL queries
def execute_query(cursor, query, data=None):
    try:
        if data:
            cursor.executemany(query, data)
        else:
            cursor.execute(query)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to create tables
def create_tables(cursor):
    tables = {
        "Client": """
            CREATE TABLE IF NOT EXISTS Client (
                Client_ID INT AUTO_INCREMENT PRIMARY KEY,
                First_name VARCHAR(50),
                Last_name VARCHAR(50),
                Email VARCHAR(100),
                Phone VARCHAR(15),
                Address VARCHAR(255)
            );
        """,
        "Account": """
            CREATE TABLE IF NOT EXISTS Account (
                Account_ID INT AUTO_INCREMENT PRIMARY KEY,
                Account_type VARCHAR(50),
                Balance DECIMAL(10, 2),
                Open_Date DATE,
                Client_ID INT,
                FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID)
            );
        """,
        "Billing": """
            CREATE TABLE IF NOT EXISTS Billing (
                Billing_ID INT AUTO_INCREMENT PRIMARY KEY,
                Billing_date DATE,
                Amount_due DECIMAL(10, 2),
                Payment_status VARCHAR(50),
                Client_ID INT,
                FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID)
            );
        """,
        "Transactions": """
            CREATE TABLE IF NOT EXISTS Transactions (
                Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
                Date DATE,
                Amount DECIMAL(10, 2),
                Type VARCHAR(50),
                Account_ID INT,
                FOREIGN KEY (Account_ID) REFERENCES Account(Account_ID)
            );
        """,
        "Employee": """
            CREATE TABLE IF NOT EXISTS Employee (
                Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(100),
                Role VARCHAR(50),
                Phone VARCHAR(15),
                Email VARCHAR(100)
            );
        """,
        "Compliance": """
            CREATE TABLE IF NOT EXISTS Compliance (
                Compliance_ID INT AUTO_INCREMENT PRIMARY KEY,
                Report_date DATE,
                Findings TEXT,
                Employee_ID INT,
                FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
            );
        """,
    }
    for table_name, table_sql in tables.items():
        print(f"Creating table {table_name}...")
        execute_query(cursor, table_sql)

# Function to insert data into tables
def insert_data(cursor):
    data = {
        "Client": [
            ("Jake", "Willson", "jake@willson.com", "555-1234", "123 Ranch Road"),
            ("Ned", "Willson", "ned@willson.com", "555-5678", "124 Ranch Road"),
            ("Phoenix", "Two Star", "phoenix@willson.com", "555-9012", "Office"),
            ("June", "Santos", "june@compliance.com", "555-3456", "Compliance Office"),
            ("John", "Doe", "john.doe@example.com", "555-7890", "456 Elm St"),
            ("Jane", "Smith", "jane.smith@example.com", "555-2345", "789 Oak St"),
        ],
        "Account": [
            ("Savings", 15000.00, "2023-01-01", 1),
            ("Checking", 5000.00, "2023-01-02", 2),
            ("Retirement", 200000.00, "2022-12-15", 3),
            ("Business", 75000.00, "2023-03-10", 4),
            ("Investment", 30000.00, "2023-02-20", 5),
            ("Savings", 10000.00, "2023-04-01", 6),
        ],
        "Billing": [
            ("2023-04-01", 150.00, "Paid", 1),
            ("2023-04-15", 200.00, "Unpaid", 2),
            ("2023-03-20", 50.00, "Paid", 3),
            ("2023-02-10", 75.00, "Unpaid", 4),
            ("2023-05-01", 100.00, "Paid", 5),
            ("2023-05-10", 250.00, "Unpaid", 6),
        ],
        "Transactions": [
            ("2023-05-01", 500.00, "Deposit", 1),
            ("2023-05-03", 100.00, "Withdrawal", 2),
            ("2023-05-05", 200.00, "Transfer", 3),
            ("2023-05-07", 300.00, "Deposit", 4),
            ("2023-05-09", 50.00, "Fee", 5),
            ("2023-05-11", 600.00, "Deposit", 6),
        ],
        "Employee": [
            ("Jake Willson", "CFA", "555-1234", "jake@willson.com"),
            ("Ned Willson", "CFA", "555-5678", "ned@willson.com"),
            ("Phoenix Two Star", "Office Manager", "555-9012", "phoenix@willson.com"),
            ("June Santos", "Compliance Manager", "555-3456", "june@compliance.com"),
            ("John Doe", "Analyst", "555-7890", "john.doe@example.com"),
            ("Jane Smith", "Advisor", "555-2345", "jane.smith@example.com"),
        ],
        "Compliance": [
            ("2023-05-01", "All regulations met.", 4),
            ("2023-04-20", "Minor issues resolved.", 4),
            ("2023-03-15", "Review pending.", 4),
            ("2023-05-10", "Audit completed.", 4),
            ("2023-02-28", "No findings.", 4),
            ("2023-01-15", "Compliance updated.", 4),
        ],
    }

    for table, rows in data.items():
        print(f"Inserting data into {table}...")
        placeholders = ", ".join(["%s"] * len(rows[0]))
        query = f"INSERT INTO {table} VALUES (NULL, {placeholders})"
        execute_query(cursor, query, rows)

# Function to display data from tables
def display_data(cursor):
    tables = ["Client", "Account", "Billing", "Transactions", "Employee", "Compliance"]
    for table in tables:
        print(f"\n-- Displaying {table} Records --")
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

# Main execution
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("Connected to MySQL database.")
    create_tables(cursor)
    insert_data(cursor)
    display_data(cursor)

    db.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    db.close()
    print("\nDatabase connection closed.")
