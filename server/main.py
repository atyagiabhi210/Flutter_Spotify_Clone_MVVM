from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, TEXT, VARCHAR, LargeBinary

import uuid
import bcrypt
#creating instance of fastapi



# to create a route we use the decorator @app.get
#@app.get("/")


#the following is a layman way
#@app.post("/")
#async def test(request: Request):
#    print((await request.body()).decode())
#    return 'Hello World ohho'

#the following is a better way used for production
#we will use pydantic

#class Test(BaseModel):
 #   name: str
#    age: int
#@app.post("/")

#def test(t:Test):
#    print(t)
#    return 'Hello World ohho'

#actual code

app= FastAPI()



class User(Base):
    __tablename__='users'

    id=Column(TEXT, primary_key=True)
    name=Column(VARCHAR(100))
    email=Column(VARCHAR(100))
    password=Column(LargeBinary)

@app.post("/signup")

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
 
    pass



Base.metadata.create_all(engine)