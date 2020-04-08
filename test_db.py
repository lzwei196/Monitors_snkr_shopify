from flask_sqlalchemy_db import db, Sites

opt = Sites.query.all()
for val in opt:
    print(val.name)