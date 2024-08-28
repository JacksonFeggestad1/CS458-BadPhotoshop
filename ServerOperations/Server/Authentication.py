import socket
import mysql.connector

# This is the file that is currently running on the server

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_ip = '192.168.0.63'
port = 54321
server_address = (server_ip, port)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening for connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

    try:
        # Receive the username and password from the client
        email = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()

        # Connect to the database
        db = mysql.connector.connect(
            host='localhost',
            user= 'Generic',
            password='1Qaz2Wsx3Edc4Rfv',
            database='capstone'
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute a query using the received username and password
        query = "SELECT * FROM userinfo WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            # Send a success message to the client
            client_socket.send('Login successful'.encode())
        else:
            # Send a failure message to the client
            client_socket.send('Login failed'.encode())

    except Exception as e:
        print('Error:', e)

    finally:
        # Close the client socket
        client_socket.close()
