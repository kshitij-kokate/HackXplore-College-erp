import os
from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Mock user data (in a real app, this would be in a database)
USERS = {
    "faculty": {"username": "faculty", "password": "faculty123", "role": "faculty"},
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = USERS.get(username)
        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/assignments')
def assignments():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('assignments.html')

@app.route('/students')
def students():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('student-management.html')

@app.route('/analytics')
def analytics():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('analytics.html')

@app.route('/github-integration')
def github_integration():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('github-integration.html')
