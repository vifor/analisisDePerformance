FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=test_db
ENV MYSQL_USER=test_user
ENV MYSQL_PASSWORD=test_password

# Copy the SQL script to the Docker image
COPY create_test_table.sql /docker-entrypoint-initdb.d/