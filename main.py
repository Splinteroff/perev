from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from database.crud import DatabaseManager
from config.db_config import settings

app = FastAPI()


class Coords(BaseModel):
    latitude: str = Field(..., example="45.3842")
    longitude: str = Field(..., example="7.1525")
    height: str = Field(..., example="1200")


class Level(BaseModel):
    winter: Optional[str] = Field(None, example="")
    summer: Optional[str] = Field(None, example="1A")
    autumn: Optional[str] = Field(None, example="")
    spring: Optional[str] = Field(None, example="")


class UserData(BaseModel):
    email: str = Field(..., example="user@example.com")
    fam: str = Field(..., example="Иванов")
    name: str = Field(..., example="Иван")
    otc: str = Field(..., example="Иванович")
    phone: str = Field(..., example="+79001234567")


class ImageData(BaseModel):
    title: str = Field(..., example="Вид с перевала")
    img: str = Field(..., example="base64encodedstring")


class PerevalData(BaseModel):
    beauty_title: str = Field(..., example="пер.")
    title: str = Field(..., example="Пхия")
    other_titles: str = Field(..., example="Триев")
    connect: str = Field(..., example="")
    add_time: str = Field(default_factory=lambda: datetime.now().isoformat())
    user: UserData
    coords: Coords
    level: Level
    images: list[ImageData]


@app.post("/submitData/")
async def submit_data(data: PerevalData):
    db_manager = DatabaseManager(settings)
    try:
        if not all([
            data.title,
            data.user.email,
            data.user.phone,
            data.coords.latitude,
            data.coords.longitude
        ]):
            raise HTTPException(status_code=400, detail="Не хватает обязательных полей")

        pereval_id = db_manager.add_pereval(data)

        return {
            "status": 200,
            "message": "Отправлено успешно",
            "id": pereval_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))