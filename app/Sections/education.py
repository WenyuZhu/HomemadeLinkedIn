#Development of a router to manage operations for user's education


from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["education"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Education not found"}},
)

#Read user's full education info by a user id
@router.get("/{user_id}/Education", response_model = List[schemas.Education])
async def read_courses(user_id: int, db: Session = Depends(get_db)):
    db_education = crud.get_education(db, user_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="Education not found")
    return db_education

#Create a education entry to a specific user
@router.post("/{user_id}/Education", response_model=schemas.Education)
def create_education(user_id: int, education: schemas.EducationCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_education(db=db, education=education, user_id=user_id)