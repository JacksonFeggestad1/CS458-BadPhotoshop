import mysql.connector

# Connect to the MySQL database  
def open_connection():
    try:
        connection = mysql.connector.connect(
            host='69.23.75.181',
            port=3306,
            user='Generic',
            password='1Qaz2Wsx3Edc4Rfv',
            database='capstone'
        )
        # print("Connected to MySQL database!")
        # print(connection)
        return connection
        
        # Perform database operations here
        
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None
    

# Mock function calls to query the database and get photos and layers based on users
    
def create_user(connection, email, password):
    # Insert a new user into the database
    query = "INSERT INTO userinfo (email, password) VALUES (%s, %s)"
    cursor = connection.cursor()
    cursor.execute(query, (email, password))
    connection.commit()
    cursor.close()
    return

def get_user_by_email(connection, email):
    # Query the database to get user based on email
    query = "SELECT userid FROM userinfo WHERE email = %s"
    cursor = connection.cursor()
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    return user

def get_photos_by_user(connection, user_id):
    # Query the database to get photos associated with the user_id
    query = "SELECT imageid, filepath FROM image JOIN imagetouser ON image.imageid=imagetouser.image_imageid JOIN userinfo on imagetouser.user_userid = userinfo.userid WHERE userinfo.userid = "" %s"
    cursor = connection.cursor()
    cursor.execute(query, (user_id,))
    photos = cursor.fetchall()
    cursor.close()
    # The result looks like this [(1, 'mockdata\\imagehere.png')]
    return photos

def new_photo(connection, user_id, filepath):
    # Insert a new photo into the database
    querys = []
    query = "INSERT INTO image (filepath) VALUES (%s)"
    querys.append(query)
    query = "INSERT INTO imagetouser (image_imageid, user_userid) VALUES (%s, %s)"
    querys.append(query)
    for q in querys:
        cursor = connection.cursor()
        cursor.execute(q, (filepath,))
        connection.commit()
        cursor.close()    
    return

def new_layer(connection, photo_id, layer_path):
    # Insert a new layer into the database
    query = "INSERT INTO layer (layerfilepath, image_imageid) values (%s,%s)"
    cursor = connection.cursor()
    cursor.execute(query, (layer_path, photo_id))
    connection.commit()
    cursor.close()
    return

def get_layers_by_photo(connection, photo_id):
    # Query the database to get layers associated with the photo_id
    query = "SELECT * FROM layer WHERE image_imageid = %s"
    cursor = connection.cursor()
    cursor.execute(query, (photo_id,))
    layers = cursor.fetchall()
    cursor.close()
    return layers

def close_connection(connection):
    connection.close()
    # print("Connection closed!")

