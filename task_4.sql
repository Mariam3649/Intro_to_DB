-- Task 4: Insert sample data into tables

USE alx_book_store;

-- Insert authors
INSERT INTO Authors (author_name) VALUES
('J.K. Rowling'),
('George R.R. Martin'),
('Agatha Christie');

-- Insert books
INSERT INTO Books (title, author_id, price, publication_date) VALUES
('Harry Potter and the Philosopher''s Stone', 1, 19.99, '1997-06-26'),
('A Game of Thrones', 2, 25.50, '1996-08-06'),
('Murder on the Orient Express', 3, 15.75, '1934-01-01');

-- Insert customers
INSERT INTO Customers (customer_id, customer_name, email, address) VALUES
(1, 'Alice Johnson', 'alice@example.com', '123 Main St'),
(2, 'Bob Smith', 'bob@example.com', '456 Oak Ave');

-- Insert orders
INSERT INTO Orders (order_id, customer_id, order_date) VALUES
(1, 1, '2025-08-01'),
(2, 2, '2025-08-05');

-- Insert order details
INSERT INTO Order_Details (orderdetailid, order_id, book_id, quantity) VALUES
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 1);
