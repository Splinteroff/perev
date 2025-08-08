from database.models import Base
from database.crud import DatabaseManager
from config.db_config import settings

if __name__ == "__main__":
    db_manager = DatabaseManager(settings)
    Base.metadata.create_all(db_manager.engine)
    print("Таблицы успешно созданы!")