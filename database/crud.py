from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

class DatabaseManager:
    def __init__(self, settings):
        self.engine = create_engine(
            f"postgresql://{settings['user']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.SessionLocal()