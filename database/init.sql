CREATE DATABASE stationery_db;

USE stationery_db;

CREATE TABLE stationery (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    maker_name VARCHAR(100),
    name VARCHAR(100) NOT NULL,
    product_code VARCHAR(50),
    price INT UNSIGNED NOT NULL,
    stock INT UNSIGNED NOT NULL,
    category VARCHAR(50) NOT NULL,
    deleted_at DATETIME DEFAULT NULL
);

CREATE TABLE user (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_administrator BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE history (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    item_id INT UNSIGNED NOT NULL,
    user_id INT UNSIGNED NOT NULL,
    operation VARCHAR(50) NOT NULL,
    quantity INT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (item_id) REFERENCES stationery(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);
