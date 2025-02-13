from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL='postgresql://postgres:Abhi1612@localhost:5432/fluttermusicapp'
#engine is the starting point form SQLAlchemy and a central point for my db
engine=create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

#using dependency injection to seamlessly tackle the instantian and closing of the db instance
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()    
