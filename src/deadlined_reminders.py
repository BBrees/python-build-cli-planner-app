from abc import ABCMeta, ABC, abstractmethod
from collections.abc import Iterable

from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable):

    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(Iterable):

    @abstractmethod
    def is_due():
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True

class DateReminder:

    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

    def is_due(self):
        return self.date < datetime.now()