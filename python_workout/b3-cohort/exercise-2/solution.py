from abc import ABC, abstractmethod


class AbstractPayment(ABC):

    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def authorize_payment(self):
        pass


    @abstractmethod
    def charge_payment(self):
        pass


    @abstractmethod
    def reverse_payment(self):
        pass


class CannotChargeError:
    pass


class CannotReverseError:
    pass
