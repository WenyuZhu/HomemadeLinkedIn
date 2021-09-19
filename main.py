from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .dependencies import get_query_token, get_token_header, get_db
from . import crud, models, schemas
from .database import SessionLocal, engine
from .Sections import courses, users, education, experience, licenses_certifications, projects, publications, skills
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router, prefix="/users")
app.include_router(courses.router, prefix="/courses")
app.include_router(education.router, prefix="/education")
app.include_router(experience.router, prefix="/experience")
app.include_router(licenses_certifications.router, prefix="/licenses_certifications")
app.include_router(projects.router, prefix="/projects")
app.include_router(publications.router, prefix="/publications")
app.include_router(skills.router, prefix="/skills")


@app.get("/")
async def root():
    return {"message": "Welcome to Homemade LinkedIn"}
