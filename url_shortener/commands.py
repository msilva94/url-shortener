from url_shortener import app, db


@app.cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()