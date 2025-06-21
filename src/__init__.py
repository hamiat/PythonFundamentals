from data.queries import (get_all_names, 
                          get_all_person_table, 
                          get_all_certificates_and_names, 
                          get_average_age,
                          join_tables_for_person_with_scrum_certificates,
                          add_certificates,
                          db_update_cert,
                          db_delete_cert)

def main():
    #get_all_person_table()
    #get_all_names()
    #get_all_certificates_and_names()
    #get_average_age()
    #join_tables_for_person_with_scrum_certificates()
    add_certificates()
    #db_update_cert()
    #db_delete_cert()

if __name__ == "__main__":
    main()