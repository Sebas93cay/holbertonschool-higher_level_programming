-- creates the database hbtn_0d_2 and the user user_0d_2
-- my second line
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
