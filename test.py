import pyodbc

server = 'DESKTOP-J9P675D'
database = 'SK_airlines'
username = r'DESKTOP-J9P675D\Kishore'
password = '181611'

# Create a connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'



try:
    conn = pyodbc.connect(connection_string)
    print("Connected successfully!")
    s=conn.execute('SELECT * FROM Table_1')
    for row in s:
        print (row)
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")