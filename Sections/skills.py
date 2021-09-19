from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db
from typing import List


router = APIRouter(
    tags=["skills"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Skills not found"}},
)

@router.get("/{user_id}/Skills", response_model = List[schemas.Skills])
async def read_skills(user_id: int, db: Session = Depends(get_db)):
    db_skills = crud.get_skills(db, user_id)
    if db_skills is None:
        raise HTTPException(status_code=404, detail="Skills not found")
    return db_skills


@router.post("/{user_id}/Skills", response_model=schemas.Skills)
def create_skill(user_id: int, skills: schemas.SkillsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_skills(db=db, skills=skills, user_id=user_id)
