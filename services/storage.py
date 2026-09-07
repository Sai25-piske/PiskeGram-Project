import os
import uuid

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from werkzeug.utils import secure_filename

from config import AWS_REGION, S3_BUCKET, S3_PREFIX

s3 = boto3.client("s3", region_name=AWS_REGION)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {
        "jpg",
        "jpeg",
        "png",
        "gif",
        "webp",
    }


def upload_file(file_obj, content_type):
    if not S3_BUCKET:
        raise ValueError("S3_BUCKET is not configured.")

    filename = secure_filename(file_obj.filename)
    extension = filename.rsplit(".", 1)[1].lower()
    object_key = f"{S3_PREFIX}/{uuid.uuid4().hex}.{extension}"

    try:
        s3.upload_fileobj(
            file_obj,
            S3_BUCKET,
            object_key,
            ExtraArgs={"ContentType": content_type or "application/octet-stream"},
        )
    except (BotoCoreError, ClientError) as exc:
        raise RuntimeError("S3 upload failed. Check your S3 bucket and IAM role.") from exc

    return {
        "image_key": object_key,
        "image_url": f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{object_key}",
    }
