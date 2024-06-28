from fastapi import APIRouter
import uuid
import bcrypt
from fastapi import HTTPException
from models.user import User
from pydantic_schemas.user_create_schema import UserCreate
from database import db



router=APIRouter()

@router.post("/signup")

def signup_user( user: UserCreate):
    #extract the data from the request
    
    print(user.name)
    print(user.email)
    print(user.password)
    #validate the data check whether user exists or not in the db
    user_db=db.query(User).filter(User.email==user.email).first()
    if user_db:
        raise HTTPException(status_code=400, detail='User already exists')
       
    #create a new user
    hashed_pw=bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    new_user=User(
        id=str(uuid.uuid4()), 
        name=user.name, 
        email=user.email, 
        password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
 
    


