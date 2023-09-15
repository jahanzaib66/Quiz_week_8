import sqlite3
import matplotlib.pyplot as plt

# Initialize empty lists for data
years = []
co2 = []
temp = []

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Define your SQL query to fetch data
sql_query = "SELECT year, co2, temperature FROM climate_data"

# Execute the query and fetch data into lists
try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    
    for row in rows:
        years.append(row[0])
        co2.append(row[1])
        temp.append(row[2])
        
except sqlite3.Error as e:
    print("SQLite error:", e)

# Close the database connection
conn.close()

# Plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

# Save the plot as an image
plt.savefig("co2_temp_1.png")

# Show the plot
plt.show()

