# -*- coding: utf-8 -*-

import hashlib

from sqlalchemy import (
    Column,
    ForeignKey,
    )
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .base import BaseModel


def get_password_digest(password):
    return hashlib.sha1(password).hexdigest()


class UserModel(BaseModel):
    __tablename__ = 'user'

    id = Column(sa.Integer, primary_key=True)
    username = Column(sa.String(255), unique=True)
    password_digest = Column(sa.String(255))

    def set_password(self, password):
        self.password_digest = get_password_digest(password)

    password = property(fset=set_password)

    def verify_password(self, password):
        return self.password_digest == get_password_digest(password)
