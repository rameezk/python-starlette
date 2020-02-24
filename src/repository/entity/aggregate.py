from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, JSON

Base = declarative_base()


class Aggregate(Base):
    __tablename__ = "aggregates"

    uuid = Column("uuid", String(length=36), nullable=False, primary_key=True)
    version = Column("version", Integer, nullable=False, default=1)
