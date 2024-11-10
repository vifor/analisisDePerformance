import mysql.connector
import os

# Retrieve database configuration from environment variables
host = os.getenv('MYSQL_HOST', 'localhost')
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', '')
database = os.getenv('MYSQL_DATABASE', '')

# Database connection setup
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = conn.cursor()

# Path to the SQL file
sql_file_path = 'create_test_table.sql'

# Read the SQL file
with open(sql_file_path, 'r', encoding='utf-8') as file:
    sql_script = file.read()

# Execute the SQL script
for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table created successfully.")