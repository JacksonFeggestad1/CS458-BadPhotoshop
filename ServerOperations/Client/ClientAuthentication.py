import hashlib
import mysql.connector
import socket
import os
import sys


def send_creds(user_email, password):
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

send_creds("GenericEmail@something.com", "Passw0rd") # This is a mock function call to test the send_creds function