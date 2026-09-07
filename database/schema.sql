CREATE DATABASE IF NOT EXISTS piskegram;

USE piskegram;


CREATE TABLE IF NOT EXISTS posts (

	    id BIGINT AUTO_INCREMENT PRIMARY KEY,

	    username VARCHAR(100) NOT NULL,

	    caption VARCHAR(500),

	    image_key VARCHAR(500) NOT NULL,

	    image_url VARCHAR(1000) NOT NULL,

	    likes INT NOT NULL DEFAULT 0,

	    created_at TIMESTAMP
	    DEFAULT CURRENT_TIMESTAMP

	);
