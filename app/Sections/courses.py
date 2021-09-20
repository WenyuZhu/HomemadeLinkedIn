#Development of a router to manage operations for user's courses
from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["courses"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Courses not found"}},
)

#Read user's full course info by a user id
@router.get("/{user_id}/Courses", response_model = List[schemas.Courses])
async def read_courses(user_id: int, db: Session = Depends(get_db)):
    db_courses = crud.get_courses(db, user_id)
    if db_courses is None:
        raise HTTPException(status_code=404, detail="Courses not found")
    return db_courses

#Create a course entry to a specific user
@router.post("/{user_id}/Courses", response_model=schemas.Courses)
def create_courses(user_id: int, courses: schemas.CoursesCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_courses(db=db, courses=courses, user_id=user_id)