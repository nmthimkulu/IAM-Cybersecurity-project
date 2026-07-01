from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
from .models import User, db

bp = Blueprint('main', __name__)

# Simple decorator for login protection
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("You must log in first.", "danger")
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash("Login successful!", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('main.index'))

    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'user')  # default to user
        user = User(username=username, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('main.index'))
    return render_template('register.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    role = session.get('role', 'user')
    if role == "admin":
        return render_template('dashboard_admin.html', username=session.get('username'))
    else:
        return render_template('dashboard.html', username=session.get('username'))

@bp.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.index'))




