import os
from datetime import datetime
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, Batch, Measurement, Action
from flask_qrcode import QRcode

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
QRcode(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command("initdb_data")
def initdb_data():
    """Init database with data for testing / demo"""

    format_dt = '%Y-%m-%d %H:%M:%S'

    batch1 = Batch(name = '0001-20210716',
                     time_start = datetime.strptime('2021-07-16 22:50:00', format_dt),
                     time_end = datetime.strptime('2021-08-05 22:30:00', format_dt),
                     time_updated = datetime.strptime('2021-09-05 22:00:00', format_dt),
                     type_id = 1,
                     style_id = 1,
                     status_id = 4,
                     user_id =1)

    batch2 = Batch(name = '0002-20210801',
                     time_start = datetime.strptime('2021-08-01 22:50:00', format_dt),
                     time_end = datetime.strptime('2021-08-16 22:30:00', format_dt),
                     time_updated = datetime.strptime('2021-09-07 22:00:00', format_dt),
                     type_id = 3,
                     style_id = 1,
                     status_id = 1,
                     user_id =2)

    batch3 = Batch(name = '0003-20210815',
                     time_start = datetime.strptime('2021-08-15 22:50:00', format_dt),
                     time_end = datetime.strptime('2021-09-05 22:30:00', format_dt),
                     time_updated = datetime.strptime('2021-09-08 22:00:00', format_dt),
                     type_id = 1,
                     style_id = 4,
                     status_id = 2,
                     user_id =1)



    db.session.add(batch1)
    db.session.add(batch2)
    db.session.add(batch3)
    
    db.session.commit()

    print("Database initialized with 3 demo batches")
