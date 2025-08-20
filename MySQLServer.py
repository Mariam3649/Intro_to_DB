import mysql.connector

def create_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      # غيريها لو عندك يوزر مختلف
            password=""       # اكتبي الباسورد لو فيه
        )

        cursor = connection.cursor()
        # Create database statement
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle exception
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()


