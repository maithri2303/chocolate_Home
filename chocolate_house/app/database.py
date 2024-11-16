from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:///chocolate_house.db', connect_args={"check_same_thread": False})
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

def init_db():
    from app.models import SeasonalFlavor, Ingredient, CustomerSuggestion

    Base.metadata.create_all(bind=engine)
