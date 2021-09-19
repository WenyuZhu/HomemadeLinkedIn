from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_token_header, get_db


router = APIRouter(
    tags=["education"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Education not found"}},
)

@router.get("/{user_id}/Education", response_model = schemas.Education)
async def read_courses(user_id: int, db: Session = Depends(get_db)):
    db_education = crud.get_education(db, user_id)
    if db_education is None:
        raise HTTPException(status_code=404, detail="Education not found")
    return db_education

@router.post("/{user_id}/Education", response_model=List[schemas.Education])
def create_education(user_id: int, education: schemas.EducationCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_education(db=db, education=education, user_id=user_id)