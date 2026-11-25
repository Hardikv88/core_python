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
            row = cur.fetchone()
        conn.commit()
        return row


def update_student(student_id: int, data: dict) -> dict | None:
    query = """
        UPDATE student_details
        SET first_name   = %(first_name)s,
            last_name    = %(last_name)s,
            birth_date   = %(birthday)s,
            phone_number = %(phone_number)s,
            country      = %(country)s,
            state        = %(state)s,
            city         = %(city)s,
            address      = %(address)s
        WHERE id = %(id)s
        RETURNING id, first_name, last_name, birth_date AS birthday, phone_number,
                  country, state, city, address
    """
    with psycopg.connect(**DATABASE, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {**data, "id": student_id})
            row = cur.fetchone()
        conn.commit()
        return row


def delete_student(student_id: int) -> bool:
    query = "DELETE FROM student_details WHERE id = %(id)s RETURNING id"
    with psycopg.connect(**DATABASE, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"id": student_id})
            deleted = cur.fetchone()
        conn.commit()
        return deleted is not None


def get_all_students() -> list[dict]:
    query = """
        SELECT id, first_name, last_name, birth_date AS birthday, phone_number,
               country, state, city, address
        FROM student_details
        ORDER BY id
    """
    with psycopg.connect(**DATABASE, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
