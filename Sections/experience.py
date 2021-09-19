from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db


router = APIRouter(
    tags=["experience"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Experience not found"}},
)

@router.get("/{user_id}/Experience", response_model = List[schemas.Experience])
async def read_experience(user_id: int, db: Session = Depends(get_db)):
    db_experience = crud.get_experience(db, user_id)
    if db_experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return db_experience


@router.post("/{user_id}/Experience", response_model=schemas.Experience)
def create_experience(user_id: int, experience: schemas.ExperienceCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_experience(db=db, experience=experience, user_id=user_id)