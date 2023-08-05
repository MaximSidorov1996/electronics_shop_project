from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sims_amount: int):
        super().__init__(name, price, quantity)
        self.__sims_amount = sims_amount

    def __repr__(self):
        return super().__repr__().replace(')', f', {self.__sims_amount})')

    @property
    def number_of_sim(self):
        return self.__sims_amount

    @number_of_sim.setter
    def number_of_sim(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__sims_amount = amount
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
