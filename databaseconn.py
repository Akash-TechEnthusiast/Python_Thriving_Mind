import mysql.connector
import datetime

# Get the current time
current_time = datetime.datetime.now()



# Replace 'your_host', 'your_user', 'your_password', and 'your_database' with your actual values.
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KGM@123$",
    database="biometric_data"
)


cursor = connection.cursor()

# Example: Execute a SELECT query and print the results
query = "SELECT id, attendancedate, createddate FROM biometric_attendancedata limit 5000;"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row[0])
    update_query = "UPDATE biometric_attendancedata SET status = %s WHERE id = %s;"
    new_email = "test@123$123"
    user_id = row[0]
    cursor.execute(update_query, (new_email, user_id))

connection.commit()
cursor.close()
connection.close()

end_time = datetime.datetime.now()
duration = end_time - current_time
print("Duration:", duration)