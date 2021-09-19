from fastapi import Header, HTTPException
from .database import SessionLocal
# Dependency


async def get_token_header(x_token: str = Header(...)):

    if x_token != "fake-super-secret-token":

        raise HTTPException(status_code=400, detail="X-Token header invalid")



async def get_query_token(token: str):
    if token != "Vinny":
        raise HTTPException(status_code=400, detail="No Vinny token provided")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



