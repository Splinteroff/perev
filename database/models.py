from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    fam = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    otc = Column(String(255))
    phone = Column(String(20), nullable=False)


class PerevalAdded(Base):
    __tablename__ = 'pereval_added'

    id = Column(Integer, primary_key=True)
    beauty_title = Column(String(255))
    title = Column(String(255), nullable=False)
    other_titles = Column(String(255))
    connect = Column(String(255))
    add_time = Column(String(255), default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(10), default='new')
    raw_data = Column(JSON)


class Coords(Base):
    __tablename__ = 'pereval_coords'

    id = Column(Integer, primary_key=True)
    pereval_id = Column(Integer, ForeignKey('pereval_added.id'))
    latitude = Column(String(50), nullable=False)
    longitude = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)


class Level(Base):
    __tablename__ = 'pereval_level'

    id = Column(Integer, primary_key=True)
    pereval_id = Column(Integer, ForeignKey('pereval_added.id'))
    winter = Column(String(50))
    summer = Column(String(50))
    autumn = Column(String(50))
    spring = Column(String(50))


class PerevalImages(Base):
    __tablename__ = 'pereval_images'

    id = Column(Integer, primary_key=True)
    pereval_id = Column(Integer, ForeignKey('pereval_added.id'))
    image_id = Column(Integer, ForeignKey('images.id'))
    title = Column(String(255))


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    date_added = Column(String(255), default=func.now())
    img = Column(String(255))