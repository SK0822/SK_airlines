import pyodbc


def connection():
    global conn
    server = 'DESKTOP-J9P675D'
    database = 'SK_airlines'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'

    try:
        conn = pyodbc.connect(connection_string)


    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
    return conn


def get_city(db_conn):
    cities = []
    for i in conn.execute('select cityname from cities'):
        cities.append(i[0])
    # print(cities)
    return cities


# get_city(connection())

def get_flight_services(db_conn):
    services = []
    for i in conn.execute('select * from flight_services'):
        services.append(i)
    return services
