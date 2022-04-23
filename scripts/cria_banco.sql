CREATE DATABASE bossow;
USE bossow;

CREATE TABLE image (
	id int NOT NULL AUTO_INCREMENT,
	img longblob NOT NULL,
	filename varchar(250) NOT NULL,
	mimetype varchar(250) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

CREATE TABLE user (
	id int NOT NULL AUTO_INCREMENT,
	email varchar(150) NOT NULL UNIQUE,
	password varchar(150) NOT NULL,
	full_name varchar(150) NOT NULL,
	role varchar(150) NOT NULL,
	created_at datetime DEFAULT CURRENT_TIMESTAMP,
	profile_picture int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (profile_picture)
		REFERENCES image(id)
);

CREATE TABLE game (
	id int NOT NULL AUTO_INCREMENT,
	title varchar(500) NOT NULL,
	release_date datetime NOT NULL,
	description text NOT NULL,
	developer varchar(250) NOT NULL,
	publisher varchar(250) NOT NULL,
	trailer_url varchar(500),
	cover_picture int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (cover_picture)
		REFERENCES image(id)
);

CREATE TABLE library_game (
	user_id int NOT NULL,
	game_id int NOT NULL,
	hours_played int DEFAULT 0,
	completion_percentage int DEFAULT 0,
	last_logged_in datetime,
	PRIMARY KEY (user_id, game_id),
	FOREIGN KEY (user_id)
		REFERENCES user(id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES game(id)
		ON DELETE CASCADE
);

CREATE TABLE screenshot (
	pic_id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	PRIMARY KEY (pic_id, user_id, game_id),
	FOREIGN KEY (pic_id)
		REFERENCES image(id)
		ON DELETE CASCADE,
	FOREIGN KEY (user_id)
		REFERENCES user(id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES game(id)
);

CREATE TABLE review (
	id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	review_text text NOT NULL,
	score int DEFAULT 0,
	date_created datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id)
		REFERENCES user(id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES game(id)
		ON DELETE CASCADE
);

CREATE TABLE complaint (
	id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	game_id int NOT NULL,
	type varchar(150) NOT NULL,
	complaint_text text NOT NULL,
	solved int DEFAULT 0,
	date_created datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id)
		REFERENCES user(id)
		ON DELETE CASCADE,
	FOREIGN KEY (game_id)
		REFERENCES game(id)
		ON DELETE CASCADE
);

CREATE TABLE note (
	id int NOT NULL AUTO_INCREMENT,
	user_id int NOT NULL,
	note_text text NOT NULL,
	date_created datetime DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id)
		REFERENCES user(id)
		ON DELETE CASCADE
);
