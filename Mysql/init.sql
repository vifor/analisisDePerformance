DELIMITER //
ALTER USER 'test_user'@'%' IDENTIFIED WITH mysql_native_password BY 'test_password';
FLUSH PRIVILEGES;
