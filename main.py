from hello import db
from hello import app
from hello import Role , User


with app.app_context():
    db.create_all()
    #admin_role = Role(name = 'Admin')
    #db.session.add(admin_role)
    #db.session.commit()
    #user_john = User(username = 'John', role = admin_role)
    #db.session.add(user_john)
    #db.session.commit()


