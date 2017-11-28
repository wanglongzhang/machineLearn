# coding: utf-8
"""
auto generate by command
sqlacodegen mysql://root:111111@10.108.92.136:3306/service_profile
"""
from sqlalchemy import BigInteger, Column, DateTime, Integer, String 
from sqlalchemy.dialects.mysql.types import LONGBLOB                 
from controller.baseController import Base
from datetime import datetime


class Application(Base):
    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    status = Column(Integer)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now)

    # def __repr__(self):
    #     #import pdb; pdb.set_trace()
    #     return json.dumps(self.to_dict(), cls=CustomizedJsonEncoder)
    #
    # def to_dict(self):
    #     return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    #
    # def __str__(self):
    #     return "Hello world, " + " (__str__)"

    # def toJSON(self):
    #     return json.dumps(self,
    #                       default=lambda o: o.__dict__,
    #                       sort_keys=True,
    #                       indent=4)


class Configuration(Base):
    __tablename__ = 'configuration'

    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, nullable=False)
    environment_id = Column(Integer, nullable=False)
    configuration = Column(LONGBLOB, nullable=False)
    masked_configuration = Column(LONGBLOB, nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now)


class Environment(Base):
    __tablename__ = 'environment'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    status = Column(Integer)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now)


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    status = Column(String(255))


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    status = Column(Integer)


class RolePermission(Base):
    __tablename__ = 'role_permission'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255))
    phone_number = Column(BigInteger)
    password = Column(String(255))
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, onupdate=datetime.now)
    status = Column(Integer)


class UserPermission(Base):
    __tablename__ = 'user_permission'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class UserRole(Base):
    __tablename__ = 'user_role'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, nullable=False)