CREATE DATABASE IF NOT EXISTS hbtn_02_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_02_2.* TO 'user_0d_2'@'localhost';