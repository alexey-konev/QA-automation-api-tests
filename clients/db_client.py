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

    def get_user_by_id(self, user_id):
        self.cursor.execute(
            """
            SELECT id, name, email
            FROM users
            WHERE id = %s
            """,
            (user_id,)
        )

        return self.cursor.fetchone()

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

    def replace_user(self, user_id, name, email):
        self.cursor.execute(
            """
            UPDATE users
            SET name = %s,
                email = %s
            WHERE id = %s
            RETURNING id, name, email;
            """,
            (name, email, user_id,)
        )

        self.connection.commit()

        return self.cursor.fetchone()

    def update_user(self, user_id, name=None, email=None):
        if name is not None and email is not None:
            self.cursor.execute(
                """
                UPDATE users
                SET name = %s,
                    email = %s
                WHERE id = %s
                RETURNING id, name, email;
                """,
                (name, email, user_id)
            )

        elif name is not None:
            self.cursor.execute(
                """
                UPDATE users
                SET name = %s
                WHERE id = %s
                RETURNING id, name, email;
                """,
                (name, user_id)
            )

        elif email is not None:
            self.cursor.execute(
                """
                UPDATE users
                SET email = %s
                WHERE id = %s
                RETURNING id, name, email;
                """,
                (email, user_id)
            )

        else:
            return self.get_user_by_id(user_id)

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