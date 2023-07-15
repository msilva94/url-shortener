from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from url_shortener import db

from .models import URL


def generate_hash():
    return uuid4().hex[:10]


def get_or_create_url(original_url):
    instance = URL.query.filter_by(original_url=original_url).first()
    if not instance:
        created = False
        while not created:
            instance = URL(original_url=original_url, hash=generate_hash())
            try:
                db.session.add(instance)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            else:
                created = True
    return instance
