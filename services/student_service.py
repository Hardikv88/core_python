import psycopg
from psycopg.rows import dict_row

from config.database import DATABASE


def insert_student(data: dict) -> dict:
    query = """
        INSERT INTO student_details (
            first_name, last_name, birth_date, phone_number,
            country, state, city, address
        )
        VALUES (
            %(first_name)s, %(last_name)s, %(birthday)s, %(phone_number)s,
            %(country)s, %(state)s, %(city)s, %(address)s
        )
        RETURNING id, first_name, last_name, birth_date AS birthday, phone_number,
                  country, state, city, address
    """
    with psycopg.connect(**DATABASE, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query, data)
            return cur.fetchone()
