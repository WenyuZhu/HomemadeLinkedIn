#Development of a router to manage operations for user's licenses and certifications

from typing import List
from .. import schemas, crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import credentials_check, get_db

#Create a router that can do a credentials check
router = APIRouter(
    tags=["license_and_certifications"],
    dependencies=[Depends(credentials_check)],
    responses={404: {"description": "License or Certifications not found"}},
)

#Read user's full license and certifications info by a user id
@router.get("/{user_id}/LicenseCertifications", response_model = List[schemas.LicenseCertifications])
async def read_license_and_certifications(user_id: int, db: Session = Depends(get_db)):
    db_license_and_certifications = crud.get_license_certifications(db, user_id)
    if db_license_and_certifications is None:
        raise HTTPException(status_code=404, detail="License or Certifications not found")
    return db_license_and_certifications

#Create a license and certification entry to a specific user
@router.post("/{user_id}/LicenseCertifications", response_model=schemas.LicenseCertifications)
def create_license_certifications(user_id: int, license_certifications: schemas.LicenseCertificationsCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_user_license_certifications(db=db, license_certifications=license_certifications, user_id=user_id)