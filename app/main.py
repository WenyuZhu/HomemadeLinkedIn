from fastapi import Depends, FastAPI, HTTPException, status
from datetime import timedelta
from sqlalchemy.orm import Session
from .dependencies import get_db, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from . import models, schemas, crud
from .database import SessionLocal, engine
from .Sections import courses, users, education, experience, licenses_certifications, projects, publications, skills
import uvicorn
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm

#  Create the database tables
models.Base.metadata.create_all(bind=engine)

# A token to authenticate user
class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(courses.router, prefix="/courses")
app.include_router(education.router, prefix="/education")
app.include_router(experience.router, prefix="/experience")
app.include_router(licenses_certifications.router, prefix="/licenses_certifications")
app.include_router(projects.router, prefix="/projects")
app.include_router(publications.router, prefix="/publications")
app.include_router(skills.router, prefix="/skills")

#  Homepage
@app.get("/")
async def root():
    return {"message": "Welcome to Homemade LinkedIn"}

#Create a JWT access token and return it
@app.post("/token", response_model=Token)
async def login_for_access_token(db : Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

#Create user entry with plain password without authentication
@app.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)