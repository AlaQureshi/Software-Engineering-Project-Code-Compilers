from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AQ:Century21!@localhost/job_portal'  # Replace with your actual database URI
db = SQLAlchemy(app)

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

@app.route('/api/jobs')
def get_jobs():
    jobs = JobListing.query.all()
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
    return jsonify(job_list)

if __name__ == '__main__':
    app.run(debug=True)
