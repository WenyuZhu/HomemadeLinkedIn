from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_token_header, get_db


router = APIRouter(
    tags=["publications"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Publications not found"}},
)

@router.get("/{user_id}/Publications", response_model = schemas.Projects)
async def read_publications(user_id: int, db: Session = Depends(get_db)):
    db_publications = crud.get_publications(db, user_id)
    if db_publications is None:
        raise HTTPException(status_code=404, detail="Publications not found")
    return db_publications


@router.post("/{user_id}/Publications", response_model=List[schemas.Publications])
def create_publications(user_id: int, publications: schemas.PublicationsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_publications(db=db, publications=publications, user_id=user_id)