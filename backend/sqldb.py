import sqlite3 

def createTable():
    connection_obj = sqlite3.connect('sql.db')
 
# cursor object
    cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS USER")

    table = """ CREATE TABLE USER (
    Email VARCHAR(255)  NOT NULL,
    User_Name CHAR(25) UNIQUE NOT NULL,
    Password CHAR(25) NOT NULL);
 """
 
    cursor_obj.execute(table)
 
    print("Table is Ready")
 
# Close the connection
    connection_obj.close()
# createTable()
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
# //example
# insertDetails("adityadattaofficial@gmail.com","Aditya","998") 
# insertBLOB("David.in","kum","34")

# insertDetails("adityadattaofficial@gmail.com","Abir","9w98")
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
userDetails = retrieveUserDetails("Rohan")
print(userDetails)


