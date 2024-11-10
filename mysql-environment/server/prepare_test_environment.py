import mysql.connector
import os
import time

# Retrieve database configuration from environment variables
host = os.getenv('MYSQL_HOST', 'mysql')
user = os.getenv('MYSQL_USER', 'test_user')
password = os.getenv('MYSQL_PASSWORD', 'test_password')
database = os.getenv('MYSQL_DATABASE', 'test_db')

# Retry logic to wait for MySQL server to be ready
max_retries = 10
retry_delay = 5  # seconds

for attempt in range(max_retries):
    try:
        # Database connection setup
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        break
    except mysql.connector.Error as err:
        print(f"Attempt {attempt + 1} of {max_retries} failed: {err}")
        time.sleep(retry_delay)
else:
    raise Exception("Could not connect to MySQL server after several attempts")

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