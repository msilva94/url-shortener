from uuid import uuid4

from url_shortener import db

from .models import URL


def generate_hash():
    return uuid4().hex[:10]


def generate_unique_hash():
    hash = generate_hash()
    while URL.query.filter_by(hash=hash).first() is not None:
        hash = generate_hash()
    return hash


def get_or_create_url(original_url):
    instance = URL.query.filter_by(original_url=original_url).first()
    if not instance:
        instance = URL(original_url=original_url, hash=generate_unique_hash())
        db.session.add(instance)
        db.session.commit()
    return instance
