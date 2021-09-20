#Development of a router to manage operations for user's profile

from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["users"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "Users not found"}},
)


#Read user's full profile info by a user id
@router.get("/{user_id}/profile", response_model = schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Query user's id by email address
@router.get("/")
def get_id_by_email(email: str, db : Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user.id

#Delete a user's row with an email address
@router.delete("/")
def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user_by_email(db=db, email=email)