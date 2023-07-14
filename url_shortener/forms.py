from flask_wtf import FlaskForm
from wtforms import StringField, validators


class URLShortenerForm(FlaskForm):
    url = StringField(
        "URL",
        [validators.DataRequired(), validators.URL()],
        render_kw={"class": "form-control my-3", "placeholder": "https://google.com"},
    )
