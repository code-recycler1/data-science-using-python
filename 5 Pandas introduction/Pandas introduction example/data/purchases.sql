-- Create the customers table
CREATE TABLE customers (
    customerId INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Create the purchases table
CREATE TABLE purchases (
    purchaseId INT PRIMARY KEY AUTO_INCREMENT,
    customerId INT,
    quantity INT,
    fruit VARCHAR(50),
    FOREIGN KEY (customerId) REFERENCES customers(customerId)
);

-- Insert customers
INSERT INTO customers (name) VALUES ('June');
INSERT INTO customers (name) VALUES ('Robert');
INSERT INTO customers (name) VALUES ('Lily');
INSERT INTO customers (name) VALUES ('David');

-- Insert purchases
-- For apples
INSERT INTO purchases (customerId, quantity, fruit) VALUES (1, 3, 'apples');
INSERT INTO purchases (customerId, quantity, fruit) VALUES (2, 2, 'apples');
INSERT INTO purchases (customerId, quantity, fruit) VALUES (4, 1, 'apples');

-- For oranges
INSERT INTO purchases (customerId, quantity, fruit) VALUES (1, 0, 'oranges');
INSERT INTO purchases (customerId, quantity, fruit) VALUES (2, 3, 'oranges');
INSERT INTO purchases (customerId, quantity, fruit) VALUES (3, 7, 'oranges');
INSERT INTO purchases (customerId, quantity, fruit) VALUES (4, 2, 'oranges');
