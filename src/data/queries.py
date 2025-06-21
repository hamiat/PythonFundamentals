import psycopg2
from .config import config

def get_all_person_table():
    create_connection(query='SELECT * FROM person;')

def create_connection(query):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = query
        cursor.execute(SQL)
        for row in cursor:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()    

