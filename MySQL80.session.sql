
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Hubcapsb109$',
    database='sql'
)
SELECT player_id, first_name, last_name, team_name 
FROM player 
INNER JOIN team 
    ON player.team_id = team.team_id;


SELECT player_id, first_name, last_name, team_name 
FROM player 
LEFT OUTER JOIN team 
    ON player.team_id = team.team_id;

SELECT player_id, first_name, last_name, team_name 
FROM player 
RIGHT OUTER JOIN team 
    ON player.team_id = team.team_id;

SELECT first_name, last_name 
FROM player 
WHERE player_id = 3;

UPDATE player 
SET team_id = 2,
    first_name = 'Gollum', 
    last_name = 'Ring Stealer'
WHERE first_name = 'Smeagol';

DELETE FROM player 
WHERE first_name = 'Smeagol';

INSERT INTO player (first_name, last_name, team_id)
    VALUES('Smeagol', 'Shire Folk', 1)


