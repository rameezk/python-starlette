from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .aggregate import Aggregate

Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    uuid = Column("uuid", String(length=36), nullable=False, primary_key=True)
    aggregate_uuid = Column(
        "aggregate_uuid",
        String(length=36),
        ForeignKey("aggregates.uuid"),
        nullable=False,
        index=True,
    )
    name = Column("name", String(length=50), nullable=False)
    data = Column("data", JSON)

    aggregate = relationship(Aggregate, uselist=False, backref="events")
