import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from generate_user_fields import get_values


try:   
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  database='db_2',
                                  port="5432",
                                  options="-c search_path=public")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    for i in range(500):
        values = get_values()
        request = f"""INSERT INTO users (email, password, first_name, last_name, patronymic, birth_date, job, nation, phone)
        VALUES ('{values["email"]}', 
        '{values["password"]}', 
        '{values["first_name"]}', 
        '{values["last_name"]}', 
        '{values["patronymic"]}',
         '{values["birth_date"]}',
          '{values["job"]}',
           '{values["nation"]}',
            '{values["phone"]}');
        """
        cursor.execute(request)
        connection.commit()

except (Exception, Error) as error:
    print(error)

finally:
    if connection:
        cursor.close()
        connection.close()
        