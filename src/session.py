import models
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def create_db_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
