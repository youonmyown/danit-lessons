import mysql.connector
import time

def wait_for_mysql():
    max_retries = 30  # Максимальное количество попыток подключения
    retries = 0

    while True:
        try:
            # Пытаемся подключиться к MySQL
            connection = mysql.connector.connect(
                host='mysql',
                user='root',
                password='rootpass'
            )

            # Если подключение успешно, выходим из цикла
            connection.close()
            print("MySQL is ready.")
            break
        except mysql.connector.Error as err:
            # Если не удалось подключиться, ждем некоторое время и пытаемся снова
            print(f"Waiting for MySQL... ({err})")
            time.sleep(1)
            retries += 1

            # Если превышено максимальное количество попыток, выводим сообщение и выходим
            if retries >= max_retries:
                print("Unable to connect to MySQL. Exiting.")
                exit(1)

# Вызываем функцию ожидания MySQL перед выполнением остальной части скрипта
wait_for_mysql()

# Создание базы данных и пользователя
connection = mysql.connector.connect(
    host='mysql',
    user='root',
    password='rootpass'
)

# Создание курсора
cursor = connection.cursor()

# Создание базы данных
cursor.execute("CREATE DATABASE IF NOT EXISTS Big_Sobaka_DB")

# Создание пользователя и предоставление прав
cursor.execute("CREATE USER IF NOT EXISTS 'kinolog'@'%' IDENTIFIED BY 'changeme'")
cursor.execute("GRANT ALL PRIVILEGES ON Big_Sobaka_DB.* TO 'kinolog'@'%'")

# Применение изменений
connection.commit()

# Закрытие соединения
cursor.close()
connection.close()
