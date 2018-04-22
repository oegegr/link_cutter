from app import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255), index=True, unique=True)
    short_url = db.Column(db.String(15), index=True)

    def __repr__(self):
        return '<Short Url:{}'.format(self.short_url)
