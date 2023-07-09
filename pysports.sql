CREATE USER 'pysports_user'@'root'IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'root';
DROP USER IF EXISTS 'pysports_user'@'root';

CREATE TABLE team (
    team_id    INT         NOT NULL     AUTO_INCREMENT,
    team_name  VARCHAR(75) NOT NULL, 
    mascot     VARCHAR(75) NOT NULL, 
    PRIMARY KEY(team_id)
);


CREATE TABLE player( 
    player_id    INT          NOT NULL     AUTO_INCREMENT,sql
    first_name   VARCHAR(75)  NOT NULL, 
    last_name    VARCHAR(75)  NOT NULL,
    team_id      INT          NOT NULL, 
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
    REFERENCES team(team_id)
);

INSERT INTO team(team_name, mascot) 
    VALUES('TEAM GANDALF', 'White Wizards');

DROP TABLE IF EXISTS player;


SELECT team_id FROM team WHERE team_name = 'Team Sauron' 
cursor = cnx.cursor()
team_query = "SELECT team_id, team_name, mascot FROM team"
INSERT INTO player(player_id)
    VALUES('123456');

config = { 
    "user": "pysports_user", 
    "password": "MySQL8IsGreat!",
    "root":3306,
    "database": "pysports",
    "raise_on_warnings": True 
}

