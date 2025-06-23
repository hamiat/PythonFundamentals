from configparser import ConfigParser
import psycopg2

def config(filename='c:/Users/Hamiat/.vscode/PythonFundamentals/src/data/database_azure.ini', section='postgresqlSection'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file.".format(section, filename)
        )

    return {
        "host": db["pghost"],
        "user": db["pguser"],
        "port": db["pgport"],
        "database": db["pgdatabase"],
        "password": db["pgpassword"]
    }

def db_general_fetch():
    conn = psycopg2.connect(**config())
    cur = conn.cursor()
    cur.execute("Select * from vendor")
    for row in cur:
        print(row)
    cur.close()
    conn.close()

def db_create_vendor(vendor, phone_no):
    con = None
    cur = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        cur.execute(
            "INSERT INTO vendor(name, contact_phone) Values (%s, %s)",
            (vendor, phone_no),
        )
        print("Row was sucessfully added.")
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)
        return None
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

def create_vendor():
    db_create_vendor('UG Electronics', '+25610485855')

def main():
    #create_vendor()
    db_general_fetch()

if __name__ == "__main__":
    main()