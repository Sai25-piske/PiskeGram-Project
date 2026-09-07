import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "zF>D4So.0Oq$rng>~6|<N<64#SGH")

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET", "piske-gram-bucket")
S3_PREFIX = os.getenv("S3_PREFIX", "uploads")

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "10.0.1.184/24"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "admin"),
    "password": os.getenv("MYSQL_PASSWORD", "zF>D4So.0Oq$rng>~6|<N<64#SGH"),
    "database": os.getenv("MYSQL_DATABASE", "piskegram"),
}
