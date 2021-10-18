from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User, Batch
from ..email import send_email
from . import main, batches
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    print('index function executed')
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))



@batches.route('/batch_overview', methods=['GET', 'POST'])
def all_batches():
    print('all_batches function executed')
    _all_batches = Batch.query.all()

    return render_template('batch_overview.html',
                           all_batches=_all_batches)

@batches.route('/view_batch/<id>', methods=['GET', 'POST'])
def view_batch(id):
    _batch = Batch.query.filter_by(id=id).first()

    if not _batch:
        #flash('Oops! Something went wrong!.', 'danger')
        return redirect(url_for("batches.all_batches"))

    return render_template('batches/view_batch.html',
                           batch=_batch)