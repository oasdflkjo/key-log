import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('key_log.db')
cursor = conn.cursor()

# Query the database
cursor.execute("SELECT * FROM key_log")
rows = cursor.fetchall()

# Print out the results
for row in rows:
    print(row)

# Close the connection
conn.close()
