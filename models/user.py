from config.db import meta
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer,String

users = Table('users', meta,
              Column('id', Integer, primary_key=True, autoincrement = True),
              Column('name', String(length=225)),
              Column('email', String(length=225)),
              Column('password', String(length=225)),
     )
