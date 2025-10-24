"""
Author: Lichao Huang
Version: 1.0.0
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract base class for all observers.
    Concrete observers must implement the update() method.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receives update messages from the subject.

        Args:
            message (str): The notification or message sent by the subject.
        """
        pass