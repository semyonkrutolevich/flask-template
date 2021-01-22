import os
from app.config import SECRET_KEY
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.main import app


app.config.from_pyfile('config.py')
# migrate = Migrate(app, db)
manager = Manager(app)

# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.app.secret_key = "sdgr24g24tgT234twfe"
    manager.run()
