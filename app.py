import os

from flask import Flask, flash, redirect, render_template, request, url_for

from config import MAX_FILE_SIZE, SECRET_KEY
from services.db_service import create_post, fetch_posts, init_db, like_post
from services.storage import allowed_file, upload_file


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    posts = fetch_posts()
    return render_template("index.html", posts=posts)


@app.post("/upload")
def upload():
    if "photo" not in request.files:
        flash("Please select a photo.")
        return redirect(url_for("index"))

    photo = request.files["photo"]
    caption = request.form.get("caption", "").strip()

    if not photo.filename:
        flash("Please select a photo.")
        return redirect(url_for("index"))

    if not allowed_file(photo.filename):
        flash("Allowed formats: JPG, JPEG, PNG, GIF and WEBP.")
        return redirect(url_for("index"))

    photo.seek(0, os.SEEK_END)
    file_size = photo.tell()
    photo.seek(0)

    if file_size > MAX_FILE_SIZE:
        flash("Maximum file size is 10 MB.")
        return redirect(url_for("index"))

    try:
        upload_result = upload_file(photo, photo.content_type)
        create_post("piske", caption or "📸 New post", upload_result["image_key"], upload_result["image_url"])
        flash("Photo uploaded to S3 and saved in MySQL! 🎉")
    except ValueError as exc:
        flash(str(exc))
    except RuntimeError as exc:
        app.logger.exception("S3 upload failed")
        flash(str(exc))
    except Exception:
        app.logger.exception("MySQL operation failed")
        flash("MySQL operation failed. Check your database configuration.")

    return redirect(url_for("index"))


@app.post("/like/<int:post_id>")
def like(post_id):
    like_post(post_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
