CREATE TABLE players (
	 player_id INT NOT NULL,
     first_name VARCHAR NOT NULL,
     last_name VARCHAR NOT NULL,
     hand VARCHAR NOT NULL,
     country_code VARCHAR NOT NULL,
     PRIMARY KEY (player_id)
);

SELECT * FROM players

CREATE TABLE matches (
	loser_age Float NOT NULL,
    loser_id INT NOT NULL,
    loser_name VARCHAR NOT NULL,
    loser_rank INT NOT NULL,
    winner_age Float NOT NULL,
	winner_id INT NOT NULL,
	winner_name VARCHAR NOT NULL,
	winner_rank INT NOT NULL
);

SELECT * FROM matches
