from fastapi import FastAPI
from database import engine

from models.base import Base
from routes import auth
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
app.include_router(router=auth.router, prefix='/auth')


Base.metadata.create_all(engine)