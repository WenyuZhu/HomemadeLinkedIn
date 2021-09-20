# This file defines pydantic model schemas which interact with frontend

from typing import List, Optional
from datetime import date
from pydantic import BaseModel


# Each of the vitals has three schemas, one base shcema to be inherited, one schema to create an entry in database, 
# and one schema to output the user info which can filter out some sensitive info
class CoursesBase(BaseModel):
    course_name: str
    number: Optional[str] = None

class CoursesCreate(CoursesBase):
    pass

class Courses(CoursesBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class EducationBase(BaseModel):
    school: str
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_data: Optional[date] = None
    end_data: Optional[date] = None
    grade: Optional[float] = None
    activities_and_societies: Optional[str] = None

class EducationCreate(EducationBase):
    pass

class Education(EducationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ExperienceBase(BaseModel):
    title: str
    employment_type: Optional[str] = None
    company_name: str
    location: Optional[str] = None
    current_working: bool
    start_data: date
    end_data: date
    description: Optional[str] = None

class ExperienceCreate(ExperienceBase):
    pass

class Experience(ExperienceBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class LicenseCertificationsBase(BaseModel):
    name: str
    issuing_organization: str
    will_expire: bool
    issue_data: Optional[date] = None
    expiration_data: Optional[date] = None
    description: Optional[str] = None
    credetial_id: Optional[str] = None
    credetial_url: Optional[str] = None

class LicenseCertificationsCreate(LicenseCertificationsBase):
    pass

class LicenseCertifications(LicenseCertificationsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class ProjectsBase(BaseModel):
    name: str
    current_working: bool
    start_data: Optional[date]
    end_data: Optional[date]
    description: Optional[str]
    project_url: Optional[str]

class ProjectsCreate(ProjectsBase):
    pass

class Projects(ProjectsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class PublicationsBase(BaseModel):
    title: str
    publisher: Optional[str] = None
    publication_date: Optional[date] = None
    authors: Optional[str] = None
    publication_URL:Optional[str] = None
    description: Optional[str] = None
    

class PublicationsCreate(PublicationsBase):
    pass

class Publications(PublicationsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class SkillsBase(BaseModel):
    name: str = None

class SkillsCreate(SkillsBase):
    pass

class Skills(SkillsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    email: str
    name: Optional[str]
    languages: Optional[str] = None
    is_member: bool = False
    about: Optional[str] = None

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    courses: Optional[List[Courses]] = []
    education: Optional[List[Education]] = []
    experience: Optional[List[Experience]] = []
    license_certifications: Optional[List[LicenseCertifications]] = []
    projects: Optional[List[Projects]] = []
    publications: Optional[List[Publications]] = []
    skills: Optional[List[Skills]] = []

    class Config:
        orm_mode = True

