from app import app
from extensions import db
from models import Task

with app.app_context():
    fixed = 0

    for task in Task.query.filter_by(is_done=True).all():
        if task.progression != 100:
            task.progression = 100
            fixed += 1

    db.session.commit()
    print(f"Tâches terminées corrigées : {fixed}")
