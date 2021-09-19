from typing import List, Optional
from datetime import date
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Boolean



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
    description: Optional[float] = None
    

class PublicationsCreate(PublicationsBase):
    pass

class Publications(PublicationsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class SkillsBase(BaseModel):
    name: str

class SkillsCreate(SkillsBase):
    pass

class Skills(SkillsBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    email: str
    name: str
    languages: Optional[str] = None
    is_member: bool = False
    about: Optional[str] = None

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    courses: List[Courses] = []
    education: List[Education] = []
    experience: List[Experience] = []
    license_certifications: List[LicenseCertifications] = []
    projects: List[Projects] = []
    publications: List[Publications] = []
    skills: List[Skills] = []

    class Config:
        orm_mode = True
