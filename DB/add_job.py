from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, JobListing

# Create a new session
DATABASE_URI = 'mysql+pymysql://AQ:Century21!@localhost/job_portal'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_job():
    job_title = "GA DOR - Developer 1 (741904)"
    job_description = (
        "Full job description\n"
        "Title: GA DOR - Developer 1 (741904)\n\n"
        "Client: State of Georgia\n\n"
        "Job ID: 741904\n\n"
        "Duration: 08/05/2024- 06/30/2025\n\n"
        "Location: 1800 Century Blvd, Atlanta, GA 30345—Hybrid\n\n"
        "Summary: Under direct supervision, designs, codes, tests, modifies and debugs computer software.\n\n"
        "Job description:\n\n"
        "*Candidate MUST be local to Metro Atlanta*\n\n"
        "*Tax Clearance Letter, due at the time of submission* (pls review compliance tab for instruction on how the CANDIDATE must obtain this letter)\n\n"
        "Job Summary:\n\n"
        "Under direct supervision, designs, codes, tests, modifies and debugs computer software. Researches and analyzes program or systems problems and develops program documentation. Translates business requirements into development activities in secure and maintainable code. Supports configuration of all aspects of the GenTax® COTS application.\n\n"
        "RECENT UNDERGRAD GRADUATE*\n\n"
        "MUST BE LOCAL METRO ATLANTA CANDIDATES*\n\n"
        "THE TAX CLEARANCE LETTER COMPLIANCE ITEM, IS DUE AT THE TIME OF CANDIDATE SUBMISSION\n\n"
        "Qualifications:\n\n"
        "Bachelor's degree from an accredited college or university with coursework in computer science or management information systems.\n\n"
        "US Citizenship or Green Card status is required\n\n"
        "Preferred Qualifications:\n\n"
        "Knowledge and experience working with software development organizations\n\n"
        "Strong analytical and problem solving skills\n\n"
        "Working knowledge of Structured Query Language (SQL)\n\n"
        "Experience in Microsoft .NET\n\n"
        "Other Notes:\n\n"
        "DOR will conduct a background check on all candidates considered for the position. Individuals must be compliant with Georgia tax obligations.\n\n"
        "Individuals having any overdue and unpaid taxes or any felony convictions (no matter how long ago) will not be offered the position or hired.\n\n"
        "All employees will be fingerprinted.\n\n"
        "Candidates must be willing to relocate to Georgia for at least the duration of the contract, if not already a resident of Georgia.\n\n"
        "Job Type: Contract\n\n"
        "Pay: $30.00 - $32.00 per hour\n\n"
        "Schedule:\n\n"
        "- Day shift\n\n"
        "Experience:\n\n"
        "- SQL: 1 year (Required)\n"
        "- .NET: 1 year (Required)\n"
        "- Software: 1 year (Required)\n"
        "- Bachelors Degree: 1 year (Required)\n\n"
        "Ability to Commute:\n\n"
        "- Atlanta, GA 30345 (Preferred)\n\n"
        "Ability to Relocate:\n\n"
        "- Atlanta, GA 30345: Relocate before starting work (Required)\n\n"
        "Work Location: In person"
    )
    location = "Atlanta, GA 30345"
    salary = 66560  # Approximate annual salary based on hourly rate
    job_type = "contract"  # Adjust the job type as needed
    application_link = "https://www.indeed.com/jobs?q=computer+science&l=atlanta%2C+ga&sc=0kf%3Ajt%28contract%29%3B&vjk=d8b930db7d0de7b1"

    # Add job listing to the database
    new_job_listing = JobListing(
        job_title=job_title,
        job_description=job_description,
        location=location,
        salary=salary,
        job_type=job_type,
        application_link=application_link,
    )

    session.add(new_job_listing)
    session.commit()

    print("Job listing added to the database.")

if __name__ == "__main__":
    add_job()
    session.close()








