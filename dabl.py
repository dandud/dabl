import os
from datetime import datetime
import click
import pandas as pd
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import *
from flask_qrcode import QRcode
from app import helpers

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db, render_as_batch=True)
QRcode(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    with app.app_context():
        db.init_app(app)
        db.create_all()
# migrate database to latest revision
    #upgrade()

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
    """Init database with base data"""
    
    inittables = ('users', 'brewtypes','brewstyles','containertypes','measurementtypes')
    
    for table in inittables:
        helpers.table_csv_import(table)

    print("Database initialized with base framework")

@app.cli.command("initdb_batch_data")
def initdb_batch_data():
    """Init database with data for testing / demo"""

    format_dt = '%Y-%m-%d %H:%M:%S'

    batch1 = Batch(name = str(datetime.now().timestamp()),
                     time_start = datetime.strptime('2021-07-16 22:50:00', format_dt),
                     time_end = datetime.strptime('2021-08-05 22:30:00', format_dt),
                     time_updated = datetime.strptime('2021-09-05 22:00:00', format_dt),
                     type_id = 1,
                     style_id = 1,
                     status_id = 4,
                     user_id =1)

    batch2 = Batch(name = str(datetime.now().timestamp()),
                     time_start = datetime.strptime('2021-08-01 22:50:00', format_dt),
                     time_end = datetime.strptime('2021-08-16 22:30:00', format_dt),
                     time_updated = datetime.strptime('2021-09-07 22:00:00', format_dt),
                     type_id = 3,
                     style_id = 1,
                     status_id = 1,
                     user_id =2)

    batch3 = Batch(name = str(datetime.now().timestamp()),
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

@app.cli.command("exportdb_data")
def exportdb_data():
    """Export data from all tables to csv files"""
    
    tables = db.engine.table_names()
    
    for table in tables:
        if isinstance(table, str):
            print('exporting ' + table)
            helpers.table_csv_export(table)

    print("Database tables exported to app/data/export")