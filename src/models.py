import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(Integer, unique=True)
    profiles = relationship("Profiles", back_populates="users")


class Profiles(Base):
    __tablename__ = 'profiles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    posts = Column(String) 
    followers = Column(Integer)
    following = Column(Integer)
    users_id = Column(Integer, ForeignKey('users.id'), unique=True)
    users = relationship("Users", back_populates="profiles")


    def to_dict(self):
        return {}


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    image_url = Column(String, nullable=False)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    comment = Column(String(300))
    posts_id = Column(Integer, ForeignKey('posts.id'))


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    posts_id = Column(Integer, ForeignKey('posts.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    posts_id = Column(Integer, ForeignKey('posts.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
