from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_token_header, get_db


router = APIRouter(
    tags=["courses"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Courses not found"}},
)

@router.get("/{user_id}/Courses", response_model = schemas.Courses)
async def read_courses(user_id: int, db: Session = Depends(get_db)):
    db_courses = crud.get_courses(db, user_id)
    if db_courses is None:
        raise HTTPException(status_code=404, detail="Courses not found")
    return db_courses


@router.post("/{user_id}/Courses", response_model=List[schemas.Courses])
def create_courses(user_id: int, courses: schemas.CoursesCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_courses(db=db, courses=courses, user_id=user_id)