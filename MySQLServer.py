#importing the file connector 

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',   # Replace with your MySQL username
            password='$qlP@55w0rd!2o24#Db' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        #handles mysql specific errors
        print(f"MyDQL Error: {e}")

    except Error as e:
        #handles other general error
        print(f"Error: {e}")


    finally:
        # Close the connection and cursor to avoid memory leaks
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()