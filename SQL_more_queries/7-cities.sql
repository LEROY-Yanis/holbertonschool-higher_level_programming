-- Creates database hbtn_0d_usa and table cities with foreign key to states.id.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(id),
	name VARCHAR(256) NOT NULL
);

