# Making a login API for the user to login to the system

import hashlib
import mysql.connector
import socket
import os


def login(user_email, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    server_ip = '69.23.75.181'
    server_port = 54321

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    sock.connect((server_ip, server_port))

    sendinguserID = user_email.encode('utf-8')

    try: 
        sock.send(sendinguserID)
        sock.send(hashed_password.encode('utf-8'))

        server_answer = sock.recv(1024).decode('utf-8')
        print(server_answer)
    except Exception as e:
        print("Error sending credentials to server: ", e)
        return
    
    sock.close()
    return server_answer

def new_user(user_email, password):
    # Hash the password
    db_unhashed_password = 'Batman2#'
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    db_password = hashlib.sha256(db_unhashed_password.encode('utf-8')).hexdigest()
    # Connect to the database and insert the new user
    server_ip = '69.23.75.181'
    server_port = 3306
    
    try:
        db = mysql.connector.connect(
            host='69.23.75.181',
            user= 'SMC', # Change this to an authorized user
            password=db_unhashed_password, # Change this to the password
            database='capstone'
        )
    except Exception as e:
        print("Error connecting to the database: ", e)
        return
    
    cursor = db.cursor()
    query = "INSERT INTO capstone.userinfo (email, password) VALUES (%s, %s)"
    values = (user_email, hashed_password)

    cursor.execute(query, values)
    db.commit()




# Test the new_user function
# new_user('test@example.com', 'password123')