CREATE DATABASE IF NOT EXISTS db_bamba;

USE db_bamba;


CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    email VARCHAR(255) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL

);


INSERT INTO users (
    email,
    password
)

VALUES (
    'dioufbamba917@gmail.com',
    '12345'
)

ON DUPLICATE KEY UPDATE
    email = email;
