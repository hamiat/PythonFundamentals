import psycopg2
from .config import config


def get_all_person_table():
    db_connection(query="SELECT * FROM person;")


def get_all_names():
    db_connection(query="SELECT name from person")


def get_all_certificates_and_names():
    db_connection(query="SELECT name, * from certificates")


def join_tables_for_person_with_scrum_certificates():
    db_connection(
        query="select * from person p inner join certificates c on p.id = c.person_id where c.name = 'Scrum'"
    )


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
        SQL = "SELECT AVG(age) FROM person;"
        cursor.execute(SQL)
        row = cursor.fetchone()
        print(f"The average age is: {row[0]:.2f}")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def add_certificates():
    # add SQL server for person who has person_id = 2
    db_create_certificate("SQL Server", 2)
    # add Azure for person who has person_id = 2
    db_create_certificate("Azure", 2)
    db_create_certificate("Scrum", 2)


def db_create_certificate(cert: str, person_id: int):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO certificates(name, person_id) Values (%s, %s)",
            (cert, person_id),
        )
        print("Row was sucessfully added.")
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def db_update_cert():
    # update certificate (column name = name), with certificate (Scrum), for person with person_id = 4
    db_update_certificate("name", "Scrum", 4)


def db_update_certificate(column_to_update, value_to_update, person_id):
    con = None
    try:
        if column_to_update not in {"name", "person_id"}:
            raise ValueError("Invalid column name")

        con = psycopg2.connect(**config())
        cursor = con.cursor()
        # Note will update ALL rows that have person_id = 4, so make sure to add the actual id in the WHERE statement if you only wish to update one single item
        query = (
            f"UPDATE  certificates SET {column_to_update} = (%s) WHERE person_id = (%s)"
        )
        cursor.execute(query, (value_to_update, person_id))
        print("Row was sucessfully updated.")
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def db_delete_cert():
    # delete certificate, with id = 13 (if we select person_id, we will delete all cerficiates for the person)
    db_delete("certificates", 13)


def db_delete(table: str, id: int):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        # Note will delete one row which corresponds to the id in the table
        query = f"DELETE FROM {table} WHERE id = (%s)"
        cursor.execute(query, (id,))
        print("Row was sucessfully deleted for id {person_id}.")
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
