from dataclasses import dataclass, asdict


@dataclass
class Event:
    def as_dict(self):
        event_as_dict = asdict(self)
        return event_as_dict
