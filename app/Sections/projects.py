#Development of a router to manage operations for user's projects

from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["projects"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Projects not found"}},
)

#Read user's full projects info by a user id
@router.get("/{user_id}/Projects", response_model = List[schemas.Projects])
async def read_projects(user_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_projects(db, user_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

#Create a project entry to a specific user
@router.post("/{user_id}/Projects", response_model=schemas.Projects)
def create_projects(user_id: int, projects: schemas.ProjectsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_projects(db=db, projects=projects, user_id=user_id)