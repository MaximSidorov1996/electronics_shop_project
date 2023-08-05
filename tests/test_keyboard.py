def test_keyboard_creation(keyboard):
    assert str(keyboard) == "Test Keyboard"
    assert str(keyboard.language) == "EN"


def test_keyboard_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
