from dataclasses import dataclass
from .event import Event


@dataclass
class OrderCreated(Event):
    user_id: int


@dataclass
class StatusChanged(Event):
    new_status: str
