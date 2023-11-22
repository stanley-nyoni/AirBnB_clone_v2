#!/usr/bin/python3
"""Database storage engine for Airbnb clone"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Defines the Database Storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialized DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password,
                                        host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current database session"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for cls in classes:
                objects.extend(self.__sesison.query(cls).all())

        result = {}
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            result[key] = obj

        
        return result

    def new(self, obj):
        """adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves/Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads obj from the current database session"""
        Base.metadata.create_all(self.__engine)
        session_orig = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_orig)
        self.__session = Session()

    def close(self):
        """Closes current session"""
        self.__session.remove()
