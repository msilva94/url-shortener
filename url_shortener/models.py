from datetime import datetime
from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from url_shortener import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=True, nullable=False)
    hash = db.Column(db.String(32), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.original_url

    @classmethod
    def get_or_create_url(cls, original_url):
        instance = cls.query.filter_by(original_url=original_url).first()
        if not instance:
            created = False
            while not created:
                hash = str(uuid4()).split("-")[0]
                instance = cls(original_url=original_url, hash=hash)
                try:
                    db.session.add(instance)
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                else:
                    created = True
        return instance
