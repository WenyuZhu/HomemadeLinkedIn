from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_token_header, get_db


router = APIRouter(
    tags=["experience"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Experience not found"}},
)

@router.get("/{user_id}/Experience", response_model = schemas.Experience)
async def read_experience(user_id: int, db: Session = Depends(get_db)):
    db_experience = crud.get_education(db, user_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return db_experience


@router.post("/{user_id}/Experience", response_model=List[schemas.Experience])
def create_experience(user_id: int, experience: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_experience(db=db, experience=experience, user_id=user_id)