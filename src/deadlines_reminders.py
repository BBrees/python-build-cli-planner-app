from abc import ABCMeta, ABC, abstractmethod
from collections.abc import Iterable

from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable):

    @abstractmethod
    def is_due():
        pass

class DeadlineReminder(Iterable):

    @abstractmethod
    def is_due():
        pass

class DateReminder:

    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

    def is_due(self):
        return self.date < datetime.now()