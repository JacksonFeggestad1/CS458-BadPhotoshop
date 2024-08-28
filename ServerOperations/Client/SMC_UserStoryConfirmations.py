'''
This file is used to confirm the user stories that were completed by Stephen.
'''
import ServerOperations.ClientSQLCommands as SQLCommands


# SQL Commands (shortened for brevity)

connection = SQLCommands.open_connection()
user_id = 1
photos = SQLCommands.get_photos_by_user(connection, user_id)
layers = SQLCommands.get_layers_by_photo(connection, photos[0][0])
print("Photos:", photos)
print("Layers:", layers)
SQLCommands.close_connection(connection)

# SFTP Documentation look at ServerOperations\Client\SFTPHowTo.txt

# Go to ServerOperations\Client\ClientAuthentication.py and run the file. If you change the email and password, you will get a different response from the server.
