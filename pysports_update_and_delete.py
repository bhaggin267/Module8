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


def select_players(): 
    select_query = """
    SELECT player_id, first_name, last_name, team_name
    FROM player 
    INNER JOIN team
    ON player.team_id = team.team_id
    """
    cursor.execute(select_query)
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
        print()

def update_player(): 
    update_query = """
    UPDATE player
    SET team_id = 1
    WHERE first_name = 'Smeagol'
    """
    cursor.execute(update_query)
    cnx.commit()

    print(" -- PLAYER UPDATED SUCCESSFULLY -- ")

def delete_player():
    delete_query = """
    DELETE FROM player
    WHERE first_name = 'Smeagol'
    """
    cursor.execute(delete_query)
    cnx.commit()

    print(" -- PLAYER DELETED SUCCESSFULLY -- ")

def select_updated_player(): 
    select_query = """
    SELECT player_id, first_name, last_name, team_name
    FROM player
    INNER JOIN team
    ON player.team_id = team.team_id
    """
    print("-- DISPLAYING PLAYER AFTER UPDATE --")
    print("Player ID:", player[0])
    print("First Name:",player[1])
    print("Last Name:", player[2])
    print("Team Name:", player[3])
    print()

cursor.close()
cnx.close()
