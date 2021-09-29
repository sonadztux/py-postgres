from connect import conn

cursor = conn.cursor()

# Fetch all rows from table
cursor.execute("SELECT * FROM inventory ORDER BY id;")
data_rows = cursor.fetchall()

# Print all rows
print("ID\tNAME\tQUANTITY")
for row in data_rows:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))

# Cleanup
conn.commit()
cursor.close()
conn.close()