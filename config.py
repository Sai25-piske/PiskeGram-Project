import os

SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "change-this-secret")

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_PREFIX = os.getenv("S3_PREFIX", "uploads")

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "piske"),
    "password": os.getenv("MYSQL_PASSWORD", "change-me"),
    "database": os.getenv("MYSQL_DATABASE", "piskegram"),
}
