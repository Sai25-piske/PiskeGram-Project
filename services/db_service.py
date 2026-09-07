import mysql.connector

from config import DB_CONFIG


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            caption VARCHAR(500),
            image_key VARCHAR(500) NOT NULL,
            image_url VARCHAR(1000) NOT NULL,
            likes INT NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.commit()
    cursor.close()
    db.close()


def fetch_posts():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT id, username, caption, image_url, likes, created_at
        FROM posts
        ORDER BY created_at DESC
        """
    )
    posts = cursor.fetchall()
    cursor.close()
    db.close()
    return posts


def create_post(username, caption, image_key, image_url):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO posts (username, caption, image_key, image_url, likes)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (username, caption, image_key, image_url, 0),
    )
    db.commit()
    cursor.close()
    db.close()


def like_post(post_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE posts SET likes = likes + 1 WHERE id = %s", (post_id,))
    db.commit()
    cursor.close()
    db.close()
