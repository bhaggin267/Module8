
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Hubcapsb109$',
    database='sql'
)

cursor = cnx.cursor()
team_query = "SELECT team_id, team_name, mascot FROM team"

# Executes team query
cursor.execute(team_query)

print("-- DISPLAYING TEAM RECORDS --")

#display the team results uses for loop to iterate
for (team_id, team_name, mascot) in cursor:
    print("team id:", team_id)
    print("team name:", team_name)
    print("Mascot:", mascot)
    print()  

# Select query for the player table
player_query = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor.execute(player_query)

# Display player records header
print("-- DISPLAYING PLAYER RECORDS --")

# Iterate over the cursor and display the player results
for (player_id, first_name, last_name, team_id) in cursor:
    print("Player ID:", player_id)
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Team ID:", team_id)
    print() 

# Closes the cursor and connection
cursor.close()
cnx.close()
