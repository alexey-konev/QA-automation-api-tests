import psycopg
from psycopg.rows import dict_row

class DatabaseClient:

    def __init__(self, host="localhost", port=5432, dbname="qa_api_db", user="postgres", password="postgres"):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

        self.connection = psycopg.connect(
            host=self.host,
            port=self.port,
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            row_factory=dict_row
        )

        self.cursor = self.connection.cursor()


    def get_user_by_email(self, email):
        self.cursor.execute(
            """
            SELECT id, name, email
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        return self.cursor.fetchone()


    def create_user(self, name, email):
        self.cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id, name, email
            """,
            (name, email,)
        )

        self.connection.commit()

        return self.cursor.fetchone()


    def delete_user(self, user_id):
        self.cursor.execute(
            """
            DELETE FROM users 
            WHERE id = %s
            RETURNING id, name, email
            """,
            (user_id,)
        )

        self.connection.commit()

        return self.cursor.fetchone()


    def close(self):
        self.cursor.close()
        self.connection.close()