#Development of a router to manage operations for user's publications

from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["publications"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Publications not found"}},
)

#Read user's full publications info by a user id
@router.get("/{user_id}/Publications", response_model = List[schemas.Publications])
async def read_publications(user_id: int, db: Session = Depends(get_db)):
    db_publications = crud.get_publications(db, user_id)
    if db_publications is None:
        raise HTTPException(status_code=404, detail="Publications not found")
    return db_publications

#Create a publication entry to a specific user
@router.post("/{user_id}/Publications", response_model=schemas.Publications)
def create_publications(user_id: int, publications: schemas.PublicationsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_publications(db=db, publications=publications, user_id=user_id)