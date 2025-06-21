import psycopg2
from .config import config

def get_all_person_table():
    db_connection(query="SELECT * FROM person;")

def get_all_names():
    db_connection(query="SELECT name from person")

def get_all_certificates_and_names():
    db_connection(query="SELECT name, * from certificates")

def join_tables_for_person_with_scrum_certificates():
    db_connection(query="select * from person p inner join certificates c on p.id = c.person_id where c.name = 'Scrum'")

def db_connection(query, single_query=False):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = query
        cursor.execute(SQL)
        for row in cursor:
            print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()    

def get_average_age():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT AVG(age) FROM person;'
        cursor.execute(SQL)
        row = cursor.fetchone()
        print(f'The average age is: {row[0]:.2f}')
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close() 