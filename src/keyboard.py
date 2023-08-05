from src.item import Item


class MixinChLang:
    def __init__(self):
        self.__lang = 'EN'

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        self.__lang = "RU" if self.__lang == "EN" else "EN"
        return self


class Keyboard(Item, MixinChLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinChLang.__init__(self)
