import sqlite3 


# Function for Convert Binary Data 
# to Human Readable Format 
# def convertToBinaryData(filename): 
	
# 	# Convert binary format to images 
# 	# or files data 
# 	with open(filename, 'rb') as file: 
# 		blobData = file.read() 
# 	return blobData 
def createTable():
    connection_obj = sqlite3.connect('sql.db')
 
# cursor object
    cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS USER")
 
# Creating table
#     table = """ CREATE TABLE USER (
#     Email VARCHAR(255) UNIQUE NOT NULL,
#     User_Name CHAR(25) UNIQUE NOT NULL,
#     Password CHAR(25),   //if image is needed to be sent
# 	Image BLOB,
# 	HasImage BOOLEAN);
#  """
    table = """ CREATE TABLE USER (
    Email VARCHAR(255) UNIQUE NOT NULL,
    User_Name CHAR(25) UNIQUE NOT NULL,
    Password CHAR(25));
 """
 
    cursor_obj.execute(table)
 
    print("Table is Ready")
 
# Close the connection
    connection_obj.close()

def insertDetails(email,username,password): 
	try: 
		
		# Using connect method for establishing 
		# a connection 
		sqliteConnection = sqlite3.connect('sql.db') 
		cursor = sqliteConnection.cursor() 
		print("Connected to SQLite") 
		
		# insert query 
		sqlite_insert_query = """ INSERT INTO User
								(email,user_name,password) VALUES (?, ?,?)"""
		
		# Converting human readable file into 
		# binary data 
		# if photo:
		# 	hasImage=1
		# 	img = convertToBinaryData(photo) 
		# else:
		# 	hasImage=0
		# 	img=None
		# Convert data into tuple format 
		data_tuple = (email,username,password) 
		
		# using cursor object executing our query 
		cursor.execute(sqlite_insert_query, data_tuple) 
		sqliteConnection.commit() 
		print("Details inserted into a table") 
		cursor.close() 

	except sqlite3.Error as error: 
		print("Failed to insert data into sqlite table", error) 
	
	finally: 
		if sqliteConnection: 
			sqliteConnection.close() 
			print("the sqlite connection is closed") 
createTable()
# insertDetails("abc@yahoo.in","Smith","998") //example
# insertBLOB("David.in","kum","34")


def retrieveUserDetails(username):
    try:
        # Connect to the SQLite database
        sqliteConnection = sqlite3.connect('sql.db') 
        cursor = sqliteConnection.cursor()
        
        # Retrieve user details from the database
        cursor.execute("SELECT * FROM USER WHERE User_Name=?", (username,))
        user_details = cursor.fetchone()
        
        # Close the cursor and connection
        cursor.close()
        sqliteConnection.close()
        
        # Check if user exists
        if user_details:
            email, user_name, password = user_details
            return {
                "Email": email,
                "Username": user_name,
                "Password": password
            }
        else:
            return {"no-user": "User not found"}
        
    except sqlite3.Error as error:
        return {"error": "Failed to retrieve user details", "details": str(error)}

# Example usage:
# userDetails = retrieveUserDetails("someusername")
# print(userDetails)


