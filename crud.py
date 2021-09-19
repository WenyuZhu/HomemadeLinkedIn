from sqlalchemy.orm import Session

from . import models, schemas
from .dependencies import get_password_hash


##########Functions for creating users' info############

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, name = user.name, languages = user.languages, is_member = user.is_member, about = user.about)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_courses(db: Session, courses: schemas.CoursesCreate, user_id: int):
    db_course = models.Courses(**courses.dict(), owner_id=user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def create_user_education(db: Session, education: schemas.EducationCreate, user_id: int):
    db_education = models.Education(**education.dict(), owner_id=user_id)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education


def create_user_experience(db: Session, experience: schemas.ExperienceCreate, user_id: int):
    db_education = models.Experience(**experience.dict(), owner_id=user_id)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    return db_education

def create_user_license_certifications(db: Session, license_certifications: schemas.LicenseCertificationsCreate, user_id: int):
    db_license_certifications = models.LicenseCertifications(**license_certifications.dict(), owner_id=user_id)
    db.add(db_license_certifications)
    db.commit()
    db.refresh(db_license_certifications)
    return db_license_certifications

def create_user_projects(db: Session, projects: schemas.ProjectsCreate, user_id: int):
    db_projects = models.Projects(**projects.dict(), owner_id=user_id)
    db.add(db_projects)
    db.commit()
    db.refresh(db_projects)
    return db_projects

def create_user_publications(db: Session, publications: schemas.PublicationsCreate, user_id: int):
    db_publications = models.Publications(**publications.dict(), owner_id=user_id)
    db.add(db_publications)
    db.commit()
    db.refresh(db_publications)
    return db_publications
    

def create_user_skills(db: Session, skills: schemas.SkillsCreate, user_id: int):
    db_skills = models.Skills(**skills.dict(), owner_id=user_id)
    db.add(db_skills)
    db.commit()
    db.refresh(db_skills)
    return db_skills






###############Functions for getting users' info########################
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_courses(db: Session, user_id: int):
    return db.query(models.Courses).filter(models.Courses.owner_id == user_id).all()

def get_education(db: Session, user_id: int):
    return db.query(models.Education).filter(models.Education.owner_id == user_id).all()

def get_experience(db: Session, user_id: int):
    return db.query(models.Experience).filter(models.Experience.owner_id == user_id).all()

def get_license_certifications(db: Session, user_id: int):
    return db.query(models.LicenseCertifications).filter(models.LicenseCertifications.owner_id == user_id).all()

def get_projects(db: Session, user_id: int):
    return db.query(models.Projects).filter(models.Projects.owner_id == user_id).all()

def get_publications(db: Session, user_id: int):
    return db.query(models.Publications).filter(models.Publications.owner_id == user_id).all()

def get_skills(db: Session, user_id: int):
    return db.query(models.Skills).filter(models.Skills.owner_id == user_id).all()



###############Functions for deleting users' info########################
def delete_user_by_email(db: Session, email: str):
    deletedRow = db.query(models.User).filter(models.User.email == email).delete()
    db.commit()
    return str(deletedRow) + " rows are deleted."

