from connect import conn

cursor = conn.cursor()

# Delete data row from table
fruit_name = input("Fruit name: ")
cursor.execute("DELETE FROM inventory WHERE name = '{}';".format(fruit_name))
print("Deleted 1 row of data")

# Cleanup
conn.commit()
cursor.close()
conn.close()