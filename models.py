from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship


from .database import Base




class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    languages = Column(String, index=True)
    hashed_password = Column(String)
    is_member = Column(Boolean, default=False)
    about = Column(String, index=True)

    courses = relationship("Courses", back_populates="owner")
    education = relationship("Education", back_populates="owner")
    experience = relationship("Experience", back_populates="owner")
    license_certifications = relationship("LicenseCertifications", back_populates="owner")
    projects = relationship("Projects", back_populates="owner")
    publications = relationship("Publications", back_populates="owner")
    skills = relationship("Skills", back_populates="owner")
    



class Courses(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, index=True)
    number = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="courses")

class Education(Base):

    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    school = Column(String, index=True)
    degree = Column(String, index=True)
    field_of_study = Column(String, index=True)
    start_data = Column(Date, index=True)
    end_data = Column(Date, index=True)
    grade = Column(Float, index=True)
    activities_and_societies = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="education")

class Experience(Base):

    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    employment_type = Column(String, index=True)
    company_name = Column(String, index=True)
    location = Column(String, index=True)
    current_working = Column(Boolean, default=False)
    start_data = Column(Date, index=True)
    end_data = Column(Date, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="experience")

class LicenseCertifications(Base):

    __tablename__ = "license_certifications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    issuing_organization = Column(String, index=True)
    will_expire = Column(Boolean, default=False)
    issue_data = Column(Date, index=True)
    expiration_data = Column(Date, index=True)
    credetial_id = Column(String, index=True)
    credetial_url = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="license_certifications")


class Projects(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    current_working = Column(Boolean, default=False)
    start_data = Column(Date, index=True)
    end_data = Column(Date, index=True)
    project_url = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="projects")


class Publications(Base):

    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    publisher = Column(String, index=True)
    publication_date = Column(Date, index=True)
    publication_URL = Column(String, index=True, unique=True)
    description = Column(String, index=True)
    authors = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="publications")
    

class Skills(Base):

    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="skills")


