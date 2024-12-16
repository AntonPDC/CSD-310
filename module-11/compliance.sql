DROP USER IF EXISTS 'Willson_user'@'localhost';
CREATE USER 'Willson_user'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'securepassword123';
GRANT ALL PRIVILEGES ON willson_financial.* TO 'Willson_user'@'localhost';
FLUSH PRIVILEGES;

USE willson_financial;


SELECT
    Employees.Name AS Employee_Name,
    COUNT(Compliance.ComplianceID) AS Total_Compliance_Reports
FROM
    Compliance
INNER JOIN
    Employee ON Compliance.EmployeeID = Employees.EmployeeID
GROUP BY
    Employee.Name;