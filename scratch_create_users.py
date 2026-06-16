from src import create_app, db
from src.models import User

app = create_app()

with app.app_context():
    if not User.query.filter_by(username='superadmin').first():
        superadmin = User(username='superadmin', is_admin=True, is_superadmin=True)
        superadmin.set_password('superadmin*A')
        db.session.add(superadmin)
        db.session.commit()
        print("Superadmin user 'superadmin' created successfully.")
    else:
        print("Superadmin user 'superadmin' already exists.")
