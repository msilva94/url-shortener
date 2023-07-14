from flask import abort, redirect, render_template, url_for

from url_shortener import app, db

from .forms import URLShortenerForm
from .models import URL


@app.route("/", methods=["GET", "POST"])
def home():
    form = URLShortenerForm()
    context = {}
    if form.validate_on_submit():
        url = URL.get_or_create_url(form.url.data)
        context["url"] = url_for("hash", hash=url.hash, _external=True)
    else:
        context["form"] = form
    return render_template("home.html", **context)


@app.route("/<hash>")
def hash(hash):
    instance = URL.query.filter_by(hash=hash).first()
    if instance:
        return redirect(instance.original_url)
    return abort(404)
