from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
import forms
from models import Task
from datetime import datetime



@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskform()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('task added to datbase')
        #print('submitted title', form.title.data)
        return redirect(url_for('index'))

    return render_template('add.html', form=form)
