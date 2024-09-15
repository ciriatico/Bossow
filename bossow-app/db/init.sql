USE bossow;

CREATE TABLE Image (
	pic_id int NOT NULL AUTO_INCREMENT,
	data longblob NOT NULL,
	file_name varchar(250) NOT NULL,
	mime_type varchar(250) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (pic_id)
);

CREATE TABLE User (
	user_id int NOT NULL AUTO_INCREMENT,
	user_email varchar(300) NOT NULL,
	password varchar(150) NOT NULL,
	full_name varchar(150) NOT NULL,
	role varchar(150) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	profile_picture int NOT NULL,
	PRIMARY KEY (user_id),
	FOREIGN KEY (profile_picture)
		REFERENCES Image(pic_id)
);

CREATE TABLE Developer (
	developer_id int NOT NULL AUTO_INCREMENT,
	developer_name varchar(150) NOT NULL,
	headquarters varchar(300) NOT NULL,
	foundation_date datetime,
	logo_picture int NOT NULL,
	PRIMARY KEY (developer_id),
	FOREIGN KEY (logo_picture)
		REFERENCES Image(pic_id)
);

CREATE TABLE Publisher (
	publisher_id int NOT NULL AUTO_INCREMENT,
	publisher_name varchar(150) NOT NULL,
	headquarters varchar(300) NOT NULL,
	foundation_date datetime,
	logo_picture int NOT NULL,
	PRIMARY KEY (publisher_id),
	FOREIGN KEY (logo_picture)
		REFERENCES Image(pic_id)
);

CREATE TABLE Game (
	game_id int NOT NULL AUTO_INCREMENT,
	game_title varchar(500) NOT NULL,
	release_date datetime NOT NULL,
	description text NOT NULL,
	developer_id int NOT NULL,
	publisher_id int NOT NULL,
	trailer_url varchar(500),
	cover_picture int NOT NULL,
	PRIMARY KEY (game_id),
	FOREIGN KEY (developer_id)
		REFERENCES Developer(developer_id),
	FOREIGN KEY (publisher_id)
		REFERENCES Publisher(publisher_id),
	FOREIGN KEY (cover_picture)
		REFERENCES Image(pic_id)
);

CREATE TABLE Library (
	user_id int NOT NULL,
	game_id int NOT NULL,
	hours_played int DEFAULT 0,
	completion_percentage int DEFAULT 0,
	last_logged_in datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (user_id, game_id),
	FOREIGN KEY (user_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
		ON DELETE CASCADE
);

CREATE TABLE Screenshot (
	pic_id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	PRIMARY KEY (pic_id, user_id, game_id),
	FOREIGN KEY (pic_id)
		REFERENCES Image(pic_id)
		ON DELETE CASCADE,
	FOREIGN KEY (user_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
);

CREATE TABLE Review (
	review_id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	review_text text NOT NULL,
	score int DEFAULT 0,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (review_id),
	FOREIGN KEY (user_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
		ON DELETE CASCADE
);

CREATE TABLE Complaint (
	complaint_id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	complaint_type varchar(150) NOT NULL,
	complaint_text text NOT NULL,
	solved int DEFAULT 0,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (complaint_id),
	FOREIGN KEY (user_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES Game(game_id)
		ON DELETE CASCADE
);

CREATE TABLE Note (
	note_id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	note_text text NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (note_id),
	FOREIGN KEY (user_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE
);

CREATE TABLE Console (
	console_id int NOT NULL AUTO_INCREMENT,
	console_name varchar(150) NOT NULL,
	specifications varchar(600),
	developer varchar(200),
	release_date datetime,
	product_picture int NOT NULL,
	PRIMARY KEY (console_id),
	FOREIGN KEY (product_picture)
		REFERENCES Image(pic_id)
);

CREATE TABLE Available (
	game_id int NOT NULL,
	console_id int NOT NULL,
	PRIMARY KEY (game_id, console_id),
	FOREIGN KEY (game_id)
		REFERENCES Game(game_id),
	FOREIGN KEY (console_id)
		REFERENCES Console(console_id)
);

CREATE TABLE News (
	news_id int NOT NULL AUTO_INCREMENT,
	news_title varchar(300) NOT NULL,
	news_text text NOT NULL,
	publication_date datetime DEFAULT CURRENT_TIMESTAMP,
	news_picture int NOT NULL,
	author_id int NOT NULL,
	PRIMARY KEY (news_id),
	FOREIGN KEY (news_picture)
		REFERENCES Image(pic_id),
	FOREIGN KEY (author_id)
		REFERENCES User(user_id)
		ON DELETE CASCADE
);

CREATE VIEW Ranking AS
SELECT game_review.game_id, game_title, cover_picture, mean_score, COUNT(user_id) AS count_library
FROM Library
INNER JOIN
(SELECT Game.game_id, game_title, cover_picture, AVG(score) AS mean_score
FROM Game
INNER JOIN Review
ON Game.game_id = Review.game_id
GROUP BY game_id) as game_review
ON Library.game_id = game_review.game_id
GROUP BY game_id
ORDER BY mean_score DESC;

DELIMITER $$
CREATE PROCEDURE `selectFilteredReview1` (value_id varchar(100))
BEGIN                
SELECT review_id, user_id, review_user.game_id, review_text, score, created_at, user_email, full_name, profile_picture, game_title, cover_picture 
FROM (
		SELECT review_id, User.user_id, game_id, review_text, score, filtered_review.created_at, user_email, full_name, profile_picture 
        FROM (
				SELECT * FROM Review 
				WHERE user_id = value_id
			) as filtered_review 
		INNER JOIN User ON filtered_review.user_id = User.user_id 
		ORDER BY created_at
	) as review_user
INNER JOIN (SELECT game_id, game_title, cover_picture FROM Game) as filtered_game ON review_user.game_id = filtered_game.game_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `selectFilteredReview2` (value_id varchar(100))
BEGIN                
SELECT review_id, user_id, review_user.game_id, review_text, score, created_at, user_email, full_name, profile_picture, game_title, cover_picture 
FROM (
		SELECT review_id, User.user_id, game_id, review_text, score, filtered_review.created_at, user_email, full_name, profile_picture 
        FROM (
				SELECT * FROM Review 
				WHERE game_id = value_id
			) as filtered_review 
		INNER JOIN User ON filtered_review.user_id = User.user_id 
		ORDER BY created_at
	) as review_user
INNER JOIN (SELECT game_id, game_title, cover_picture FROM Game) as filtered_game ON review_user.game_id = filtered_game.game_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `selectLibrary` (value_id varchar(100))
BEGIN                
SELECT user_id, Game.game_id, hours_played, completion_percentage, last_logged_in, game_title, release_date, description, developer_id, publisher_id, trailer_url, cover_picture 
FROM (
		SELECT * 
        FROM Library 
        WHERE user_id = value_id
	) as filtered_library 
INNER JOIN Game ON filtered_library.game_id = Game.game_id;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE `selectComplaint` (coluna varchar(100), value_id varchar(100))
BEGIN
SET @sql = CONCAT('SELECT complaint_id, User.user_id, full_name, profile_picture, game_id, complaint_type, complaint_text, solved, complaint_game.created_at, game_title, cover_picture 
					FROM (
							SELECT complaint_id, user_id, Complaint.game_id, complaint_type, complaint_text, solved, Complaint.created_at, game_title, cover_picture 
							FROM Complaint INNER JOIN Game ON Complaint.game_id = Game.game_id WHERE ', coluna, '= ', value_id,
						') as complaint_game 
					INNER JOIN User ON complaint_game.user_id = User.user_id ORDER BY created_at'
				);

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;