from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    about = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), onupdate=func.now())

    # one-to-many
    pins = db.relationship("Pin", back_populates="user",
                           cascade="all, delete-orphan")

    # many-to-many
    comments = db.relationship(
        "Comment", back_populates="user", cascade="all, delete-orphan")

    board_users = db.relationship('BoardUser', back_populates='users')
    favorite = db.relationship(
        'Favorite', back_populates='user', cascade="all, delete-orphan")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'photo_url': self.photo_url,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'about': self.about
        }

    def to_dict_simple(self):
        return {
            'id': self.id,
            'photo_url': self.photo_url,
            'updated_at': self.updated_at
        }
