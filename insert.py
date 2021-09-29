from connect import conn

cursor = conn.cursor()

# Insert some data into the table
fruit_name = input("Fruit name: ")
quantity = int(input("New quantity: "))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", (fruit_name, quantity))
print("[OK] Inserted 1 rows of data")

# Clean up
conn.commit()
cursor.close()
conn.close()