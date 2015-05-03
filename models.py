from app import db


class BlogPost(db.Model):

    __tablename__ = "posts"
    __table_args__ = {'extend_existing':True}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)


    def __init__(self, title, content):
        self.title = title
        self.content = content


    def __repr__(self):
        return '<{}>'.format(self.title)

