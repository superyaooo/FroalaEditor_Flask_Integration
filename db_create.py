from app import db
from models import BlogPost


#run when adding new columns in testing, will delete previous data.
#db.drop_all()

db.create_all()

db.session.add(BlogPost("chicken feet","7 chicken feet"))
db.session.add(BlogPost("test","testing ingredients"))



db.session.commit()
