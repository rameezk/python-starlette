import typing

from domain.events.event import Event


class EventStream:
    events: typing.List[Event]
    version: int

    def __init__(self, events: typing.List[Event], version: int = 1):
        self.events = events
        self.version = version
