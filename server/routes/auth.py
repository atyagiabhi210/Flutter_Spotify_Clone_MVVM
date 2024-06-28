from fastapi import APIRouter, Depends
import uuid
import bcrypt
from fastapi import HTTPException
from database import get_db
from models.user import User
from pydantic_schemas.user_create_schema import UserCreate
from pydantic_schemas.user_login_schema import UserLogin




router=APIRouter()

@router.post("/signup",status_code=201, response_model=UserCreate)

def signup_user( user: UserCreate, db=Depends(get_db)):
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
 
@router.post("/login") 
def login_User(user: UserLogin, db= Depends(get_db)):  
    #check whether a user exists or not

    user_db=db.query(User).filter(User.email==user.email).first()
    if not user_db:
        raise HTTPException(status_code=400, detail='User does not exist')
    
   #check password
    is_match=bcrypt.checkpw(user.password.encode(), user_db.password)

    if not is_match:
        raise HTTPException(status_code=400, detail='Invalid Credentials')

    
    return user_db


