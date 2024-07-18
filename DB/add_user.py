from sqlalchemy import create_engine, Column, Integer, String, Enum, TIMESTAMP, func
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User
import hashlib

# Create a new session
DATABASE_URI = 'mysql+pymysql://AQ:Century21!@localhost/job_portal'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user():
    username = "dummy"
    password = "dummy"
    email = "dummy@example.com"
    first_name = "Dum"
    last_name = "My"
    user_type = "job_seeker"  # Adjust as per your Enum definition either job_seeker or employer

    # Hash the password
    password_hash = hash_password(password)

    # Add user to the database
    new_user = User(
        username=username,
        password_hash=password_hash,
        email=email,
        first_name=first_name,
        last_name=last_name,
        user_type=user_type,
    )

    session.add(new_user)
    session.commit()

    print("User added to the database.")

if __name__ == "__main__":
    add_user()
    session.close()
