import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Test Item", 100.0, 5)


@pytest.fixture
def phone():
    return Phone("Test Phone", 500.0, 10, 1)


@pytest.fixture
def keyboard():
    return Keyboard("Test Keyboard", 800.0, 7)
