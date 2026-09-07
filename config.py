import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ["FLASK_SECRET_KEY"]

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET", "piske-gram-bucket")
S3_PREFIX = os.getenv("S3_PREFIX", "uploads")

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost").strip(),
    "port": int(os.getenv("MYSQL_PORT", "3306").strip()),
    "user": os.getenv("MYSQL_USER", "admin").strip(),
    "password": os.environ["MYSQL_PASSWORD"],
    "database": os.getenv("MYSQL_DATABASE", "piske-gram").strip(),
}
