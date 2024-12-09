-- Create the database
CREATE DATABASE IF NOT EXISTS willson_financial;

-- Use the database
USE willson_financial;

-- Create a new user 'local_user' with a password
CREATE USER 'local_user'@'localhost' IDENTIFIED BY 'secure_password';

-- Grant all privileges to the new user for the 'willson_financial' database
GRANT ALL PRIVILEGES ON willson_financial.* TO 'local_user'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

-- Create Client table
CREATE TABLE Client (
    Client_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    Address VARCHAR(255)
);

-- Create Account table
CREATE TABLE Account (
    Account_ID INT AUTO_INCREMENT PRIMARY KEY,
    Account_type VARCHAR(50),
    Balance DECIMAL(15, 2),
    Open_Date DATE,
    Client_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID)
);

-- Create Billing table
CREATE TABLE Billing (
    Billing_ID INT AUTO_INCREMENT PRIMARY KEY,
    Billing_date DATE,
    Amount_due DECIMAL(15, 2),
    Payment_status VARCHAR(50),
    Client_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID)
);

-- Create Transactions table
CREATE TABLE Transactions (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    Amount DECIMAL(15, 2),
    Type VARCHAR(50),
    Account_ID INT,
    FOREIGN KEY (Account_ID) REFERENCES Account(Account_ID)
);

-- Create Employee table
CREATE TABLE Employee (
    Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Role VARCHAR(50),
    Phone VARCHAR(15),
    Email VARCHAR(100)
);

-- Create Compliance table
CREATE TABLE Compliance (
    Compliance_ID INT AUTO_INCREMENT PRIMARY KEY,
    Report_date DATE,
    Findings TEXT,
    Employee_ID INT,
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);

-- Confirm user privileges
SHOW GRANTS FOR 'local_user'@'localhost';
