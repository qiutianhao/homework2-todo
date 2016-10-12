from . import ModelMixin
from . import db
from . import cur_time
import json


class Todo(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.String())

    def __init__(self, form):
        self.task = form.get('task')
        self.created_time = cur_time()

    def json(self):
        j = {
            'id': self.id,
            'task': self.task,
            'created_time': self.created_time,
        }
        return json.dumps(j, ensure_ascii=False)
