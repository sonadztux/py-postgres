from connect import conn

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute('DROP TABLE IF EXISTS inventory;')
print('[OK] Finished dropping table (if existed)')

# Create a table
cursor.execute('CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);')
print("[OK] Finished creating table")

# Insert some data into the table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("[OK] Inserted 3 rows of data")

# Clean up
conn.commit()
cursor.close()
conn.close()