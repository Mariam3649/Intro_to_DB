import mysql.connector

try:
    # connect to mysql server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # ضيفي الباسورد لو عندك باسورد ل mysql
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore;")
        print("Database alxbookstore created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()

