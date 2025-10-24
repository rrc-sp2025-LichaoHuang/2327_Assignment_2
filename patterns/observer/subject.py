"""
Author: Lichao Huang
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer


class Subject(ABC):
    """
    Abstract Subject class.
    Maintains a list of observers and provides base methods for 
    attaching, detaching, and notifying them.
    """

    def __init__(self) -> None:
        """
        Initializes the Subject with an empty observer list.
        """
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the list if not already attached.

        Args:
            observer (Observer): The observer instance to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the list if it exists.

        Args:
            observer (Observer): The observer instance to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Sends a message to all attached observers.

        Args:
            message (str): The notification message to send.
        """
        for observer in self._observers:
            observer.update(message)

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method for subclasses to implement string representation.
        This enforces that all concrete subjects (like BankAccount)
        define their own __str__ method.
        """
        pass