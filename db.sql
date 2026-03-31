create database IF NOT EXISTS BookStore1;
use BookStore1;


CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(100),
    price FLOAT,
    stock INT,
    image_url TEXT,
    description TEXT
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

INSERT INTO books (title, author, category, price, stock, image_url, description) VALUES
('Atomic Habits','James Clear','Self Help',499,10,'https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg','Build good habits'),
('Rich Dad Poor Dad','Robert Kiyosaki','Finance',399,10,'https://images-na.ssl-images-amazon.com/images/I/81bsw6fnUiL.jpg','Financial education'),
('The Alchemist','Paulo Coelho','Fiction',299,10,'https://images-na.ssl-images-amazon.com/images/I/71aFt4+OTOL.jpg','Journey story'),
('Deep Work','Cal Newport','Productivity',450,10,'https://images-na.ssl-images-amazon.com/images/I/71g2ednj0JL.jpg','Focus deeply'),
('Clean Code','Robert Martin','Programming',699,10,'https://images-na.ssl-images-amazon.com/images/I/41xShlnTZTL.jpg','Coding best practices'),
('Think and Grow Rich','Napoleon Hill','Finance',350,10,'https://images-na.ssl-images-amazon.com/images/I/71UypkUjStL.jpg','Success mindset');



INSERT INTO users (username, password)
VALUES ('admin', 'admin');