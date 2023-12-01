import mysql.connector
import time

def wait_for_mysql():
    max_retries = 30
    retries = 0

    while True:
        try:
            connection = mysql.connector.connect(
                host='mysql',
                user='root',
                password='rootpass'
            )

            connection.close()
            print("MySQL is ready.")
            break
        except mysql.connector.Error as err:
            
            print(f"Waiting for MySQL... ({err})")
            time.sleep(1)
            retries += 1

            if retries >= max_retries:
                print("Unable to connect to MySQL. Exiting.")
                exit(1)

wait_for_mysql()

connection = mysql.connector.connect(
    host='mysql',
    user='root',
    password='rootpass'
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Big_Sobaka_DB")

cursor.execute("CREATE USER IF NOT EXISTS 'kinolog'@'%' IDENTIFIED BY 'changeme'")
cursor.execute("GRANT ALL PRIVILEGES ON Big_Sobaka_DB.* TO 'kinolog'@'%'")

connection.commit()

cursor.close()
connection.close()
