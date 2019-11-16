from solution import AbstractPayment, CannotChargeError, CannotReverseError
import random
import pytest

def test_not_implement_anything():
    class MyNewPayment(AbstractPayment):
        pass

    with pytest.raises(TypeError):
        mnp = MyNewPayment()


def test_not_implement_authorize():
    class MyNewPayment(AbstractPayment):
        def charge_payment(self):
            pass

        def reverse_payment(self):
            pass

    with pytest.raises(TypeError) as e:
        mnp = MyNewPayment()
        assert 'authorize_payment' in str(e)
        assert 'charge_payment' in str(e)
        assert 'reverse_payment' in str(e)


def test_not_implement_reverse():
    class MyNewPayment(AbstractPayment):
        def charge_payment(self):
            pass

        def authorize_payment(self):
            pass

    with pytest.raises(TypeError) as e:
        mnp = MyNewPayment()
        assert 'reverse_payment' in str(e)


def test_not_implement_charge():
    class MyNewPayment(AbstractPayment):
        def reverse_payment(self):
            pass

        def authorize_payment(self):
            pass

    with pytest.raises(TypeError) as e:
        mnp = MyNewPayment()
        assert 'charge_payment' in str(e)


def test_working_new_payment():
    class MyNewPayment(AbstractPayment):
        def authorize_payment(self, user_id, amount, currency):
            return True

        def charge_payment(self, user_id, amount, currency, merchant_id):
            if amount < 0 or amount > 1000:
                raise CannotChargeError(
                    f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

            return 10

        def reverse_payment(self, user_id, amount, currency, merchant_id):
            if amount < 0 or amount > 1000:
                raise CannotReverseError(
                    f"user_id {user_id}, amount {amount}, currency {currency}, merchant_id {merchant_id}")

            return 10


    mnp = MyNewPayment()
    authorize_result = mnp.authorize_payment(1, 100, 'usd')
    assert authorize_result

    charge_result = mnp.charge_payment(1, 100, 'usd', 2)
    assert charge_result == 10

    with pytest.raises(CannotChargeError) as e:
        charge_result = mnp.charge_payment(1, -5, 'usd', 2)

    with pytest.raises(CannotChargeError) as e:
        charge_result = mnp.charge_payment(1, 2000, 'usd', 2)

    reverse_result = mnp.reverse_payment(1, 100, 'usd', 2)
    assert reverse_result == 10

    with pytest.raises(CannotReverseError) as e:
        reverse_result = mnp.reverse_payment(1, -5, 'usd', 2)

    with pytest.raises(CannotReverseError) as e:
        reverse_result = mnp.reverse_payment(1, 2000, 'usd', 2)
