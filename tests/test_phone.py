import pytest

from src.phone import Phone


def test_phone_creation(phone):
    assert phone.name == "Test Phone"
    assert phone.price == 500.0
    assert phone.quantity == 10
    assert phone.number_of_sim == 1


def test_phone_repr():
    phone = Phone("Samsung Galaxy", 799.99, 3, 1)
    assert repr(phone) == "Phone('Samsung Galaxy', 799.99, 3, 1)"


def test_phone_number_of_sim_setter():
    phone = Phone("Nokia", 299.99, 2, 1)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_phone_number_of_sim_setter_invalid_value(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
