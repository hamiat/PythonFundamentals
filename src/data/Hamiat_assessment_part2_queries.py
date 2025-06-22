import psycopg2
from Hamiat_assessment_part2_config import config


def db_general_queries(query):
    con = None
    cur = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        SQL = query
        cur.execute(SQL)
        for row in cur:
            print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error: ", error)
        return None
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

# Task 5
def db_create_flights(flight_no: str, dep_time: str, arr_time:str, dep_airport:str, des_airport:str):
    con = None
    cur = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        cur.execute("INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) Values (%s, %s, %s, %s, %s)", (flight_no, dep_time, arr_time, dep_airport, des_airport))
        con.commit()
        print("Row was sucessfully added.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error: ", error)
        return None
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

def create_flights():
    db_create_flights("E2345T", "2025-12-09 12:12 AM", "2025-12-09 03:10 PM", "Stockholm Arlanda Airport", "Barcelona Airport")

    db_create_flights("F2345T", "2025-01-09 10:25 AM", "2025-01-09 02:10 PM", "Barcelona Airport", " Helsingfors-Vanda Airport",)  

    db_create_flights("G2345T", "2025-02-09 12:12 AM", "2025-02-09 03:10 PM", "Kiruna Airport", "Barcelona Airport") 

# Task 7
def db_create_airline_table():
    con = None
    cur = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        cur.execute("CREATE TABLE airline (id SERIAL PRIMARY KEY, name varchar(255) NOT NULL, flights_id INT REFERENCES flights(id) ON DELETE CASCADE)")
        con.commit()
        print("Table was sucessfully created.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error: ", error)
        return None
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

# Task 8
def db_create_airline_data(name: str, flight_id: int):
    con = None
    cur = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        cur.execute("INSERT INTO airline (name, flights_id) Values (%s, %s)", (name, flight_id))
        con.commit()
        print("Row was sucessfully added.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error: ", error)
        return None
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

def create_airline_data():
    db_create_airline_data("Sas Airlines", 1)
    db_create_airline_data("Finnair ", 2)
    db_create_airline_data("Finnair", 3)
    db_create_airline_data("Ryanair", 4)
    db_create_airline_data("Sas Airlines", 5)
    db_create_airline_data("Ryanair", 6)

# Task 10
def db_delete_general(table: str, id:int):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        query = f"DELETE FROM {table} WHERE id = (%s)"
        cursor.execute(query, (id,))
        print(f"Row was sucessfully deleted for id: {id}.")
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

def delete_from_db():
    db_delete_general("flights", 2)

if __name__ == "__main__":
   # Task 5
   create_flights()

   # Task 6
   db_general_queries("SELECT *  FROM flights ORDER BY departure_time")

   # Task 7
   db_create_airline_table()

   # Task 8
   create_airline_data()

   # Task 9
   db_general_queries("SELECT *  FROM flights f JOIN airline a on f.id = a.flights_id ORDER BY a.name ASC")

   # Task 10
   delete_from_db()


