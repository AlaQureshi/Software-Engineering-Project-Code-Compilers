from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import logging
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AQ:Century21!@localhost/job_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

logging.basicConfig(level=logging.DEBUG)

# User model
class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Store hashed passwords

# JobListing model
class JobListing(db.Model):
    __tablename__ = 'JobListings'
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    job_title = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100))
    salary = db.Column(db.Numeric(10, 2))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    application_deadline = db.Column(db.Date)
    job_type = db.Column(db.String(255))
    application_link = db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = JobListing.query.all()
        logging.debug(f'Number of jobs found: {len(jobs)}')
        job_list = []
        for job in jobs:
            job_dict = {
                'job_title': job.job_title,
                'job_description': job.job_description,
                'location': job.location,
                'salary': float(job.salary) if job.salary else None,
                'date_posted': job.date_posted.strftime('%Y-%m-%d') if job.date_posted else None,
                'application_deadline': job.application_deadline.strftime('%Y-%m-%d') if job.application_deadline else None,
                'job_type': job.job_type,
                'application_link': job.application_link
            }
            job_list.append(job_dict)
        logging.debug(f'Job list: {job_list}')
        return jsonify(job_list)
    except Exception as e:
        logging.error(f'Error fetching jobs: {e}')
        return jsonify([]), 500

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        logging.debug(f"Attempting login for user: {username}")
        user = Users.query.filter_by(username=username).first()
        
        if user:
            logging.debug(f"User found: {user.username}, checking password...")
        else:
            logging.debug(f"User {username} not found in database.")
        
        if user and user.password_hash == hash_password(password):
            logging.debug("Password check successful.")
            session['user_id'] = user.user_id
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            logging.debug("Invalid username or password.")
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

