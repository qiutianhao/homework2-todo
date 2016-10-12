from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import db

from models.todo import Todo

app = Flask(__name__)
db_path = 'todo.sqlite'
manager = Manager(app)


def register_routes(app):
    from routes.todo import main as routes_todo
    app.register_blueprint(routes_todo, url_prefix='/todo')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'qiu'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
