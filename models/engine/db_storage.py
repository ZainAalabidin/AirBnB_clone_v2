#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import os
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}

class DBStorage:
    """Interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True
        )
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            return {obj.__class__.__name__ + "." + obj.id: obj
                    for obj in self.__session.query(cls).all()}
        else:
            obj_dict = {}
            for class_name, class_type in classes.items():
                if class_name == "BaseModel":
                    continue
                for obj in self.__session.query(class_type).all():
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()
