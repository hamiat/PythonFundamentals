from configparser import ConfigParser

# Task 4 
def config(
        file = "c:/Users/Hamiat/.vscode/PythonFundamentals/src/data/Hamiat_assessment_database.ini",
        section = "postgresql" ):
    parser = ConfigParser()
    parser.read(file)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file.".format(section, file)
        )
    
    return db
    