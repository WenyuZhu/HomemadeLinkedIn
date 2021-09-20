#This file provides various dependencies, including hashing a password, get the database, credentials check, verify_password, 

from .database import SessionLocal
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from . import models
from datetime import datetime, timedelta
from typing import Optional

#Secret key and algorithm to encode and decode the JSON web tokens
SECRET_KEY  = "5df87158db30d356e93f8e2356c6607806e3b748fa01d9a457dd58c200b82ee1"
ALGORITHM = "HS256"

#Expire time for access token in minute.
ACCESS_TOKEN_EXPIRE_MINUTES = 30


#Create an instance of the OAuth2PasswordBearer class. The parameter contains the URL that the client will use to send the username and password in order to get a token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#This will be used to hash and verify passwords.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#Hashing a password
def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Credentials check for some of the read or save operations
async def credentials_check(db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

#Verify password if the input password is the same with the stored hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#Authenticate user
def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

#Create a hashed token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt