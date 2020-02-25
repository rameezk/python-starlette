import abc
import typing
import uuid

from repository.stream.event_stream import EventStream
from domain.events.event import Event


class EventStore(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load_stream(self, aggregate_uuid: uuid.UUID) -> EventStream:
        pass

    @abc.abstractmethod
    def append_to_stream(
        self,
        aggregate_uuid: uuid.UUID,
        expected_version: typing.Optional[int],
        events: typing.List[Event],
    ):
        pass


class ConcurrentStreamWriteError(RuntimeError):
    pass
