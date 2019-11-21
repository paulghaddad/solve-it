from abc import ABC, abstractmethod
import random


class AbstractPayment(ABC):

    @abstractmethod
    def authorize_payment(self):
        pass


    @abstractmethod
    def charge_payment(self):
        pass


    @abstractmethod
    def reverse_payment(self):
        pass


class CannotChargeError(Exception):
    pass


class CannotReverseError(Exception):
    pass

class MyNewPayment(AbstractPayment):

    def authorize_payment(self, user_id, amount, currency):
        return True

    def charge_payment(self, user_id, amount, currency, merchant_id):
        if amount < 0 or amount > 1000:
            raise CannotChargeError(
                f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

        return random.randint(0, 100000)

    def reverse_payment(self, user_id, amount, currency, merchant_id):
        if amount < 0 or amount > 1000:
            raise CannotReverseError(
                f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

        return random.randint(0, 100000)


mnp = MyNewPayment()
authorize_result = mnp.authorize_payment(1, 100, 'usd')
print(f"authorize_result = {authorize_result}")

print("Charging")
charge_result = mnp.charge_payment(1, 100, 'usd', 2)
print(f"charge_result = {charge_result}")

try:
    charge_result = mnp.charge_payment(1, -5, 'usd', 2)
    print(f"charge_result = {charge_result}")
except CannotChargeError as e:
    print(f"Cannot charge: {e}")

try:
    charge_result = mnp.charge_payment(1, 2000, 'usd', 2)
    print(f"charge_result = {charge_result}")
except CannotChargeError as e:
    print(f"Cannot charge: {e}")

print("Reversing")
reverse_result = mnp.reverse_payment(1, 100, 'usd', 2)
print(f"reverse_result = {reverse_result}")

try:
    reverse_result = mnp.reverse_payment(1, -5, 'usd', 2)
    print(f"reverse_result = {reverse_result}")
except CannotReverseError as e:
    print(f"Cannot reverse: {e}")

try:
    reverse_result = mnp.reverse_payment(1, 2000, 'usd', 2)
    print(f"reverse_result = {reverse_result}")
except CannotReverseError as e:
    print(f"Cannot reverse: {e}")
