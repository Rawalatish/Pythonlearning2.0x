
from abc import ABC, abstractmethod

class ATB(ABC):

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass

class Amit(ATB):

    def perform_task1(self):
        return "bow bow"

    def perform_task2(self):
        return "mow mow"


amit = Amit()
amit.perform_task1()
amit.perform_task2()