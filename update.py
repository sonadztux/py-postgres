from connect import conn

cursor = conn.cursor()

# Update a data row in the table
fruit_name = input("Fruit name: ")
quantity = int(input("New quantity: "))
cursor.execute("UPDATE inventory SET quantity = {} WHERE name = '{}';".format(quantity, fruit_name))
print("Updated 1 row of data")

# Clean up
conn.commit()
cursor.close()
conn.close()