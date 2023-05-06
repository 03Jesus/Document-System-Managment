import json
from document import Document
from datetime import date


class Sell (object):
    """
    A class that represents a Sell
    """

    def __init__(self,
                 id: int = 0,
                 date: date = date.today(),
                 pay_method: str = 'pay_method',
                 total_price: float = 0.1,
                 items: list = [Document()]) -> object:
        """
        Constructor of the class
        :param id: the id of the Sell
        :type id: int
        :param date: the date of the Sell
        :type date: date
        :param pay_method: the pay_method of the Sell
        :type pay_method: str
        :param total_price: the total_price of the Sell
        :type total_price: float
        :param items: the items of the Sell
        :type items: list
        """
        self.__id = id
        self.__date = date
        self.__pay_method = pay_method
        self.__total_price = total_price
        self.__items = items

    @property
    def id(self) -> int:
        """
        Getter for the id of the Sell
        :return: the id of the Sell
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Sell
        :param id: the new id of the Sell
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def date(self) -> date:
        """
        Getter for the date of the Sell
        :return: the date of the Sell
        :rtype: date
        """
        return self.__date

    @date.setter
    def date(self, date: date) -> None:
        """
        Setter for the date of the Sell
        :param date: the new date of the Sell
        :type date: date
        :return: None
        """
        self.__date = date

    @property
    def pay_method(self) -> str:
        """
        Getter for the pay_method of the Sell
        :return: the pay_method of the Sell
        :rtype: str
        """
        return self.__pay_method

    @pay_method.setter
    def pay_method(self, pay_method: str) -> None:
        """
        Setter for the pay_method of the Sell
        :param pay_method: the new pay_method of the Sell
        :type pay_method: str
        :return: None
        """
        self.__pay_method = pay_method

    @property
    def total_price(self) -> float:
        """
        Getter for the total_price of the Sell
        :return: the total_price of the Sell
        :rtype: float
        """
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float) -> None:
        """
        Setter for the total_price of the Sell
        :param total_price: the new total_price of the Sell
        :type total_price: float
        :return: None
        """
        self.__total_price = total_price

    @property
    def items(self) -> list:
        """
        Getter for the items of the Sell
        :return: the items of the Sell
        :rtype: list
        """
        return self.__items

    @items.setter
    def items(self, items: list) -> None:
        """
        Setter for the items of the Sell
        :param items: the new items of the Sell
        :type items: list
        :return: None
        """
        self.__items = items

    def __str__(self) -> str:
        """
        String representation of the Sell
        :return: the string representation of the Sell
        :rtype: str
        """
        return {"id": self.__id,
                "date": self.__date,
                "pay_method": self.__pay_method,
                "total_price": self.__total_price,
                "items": self.__items}

    def __eq__(self, other: object) -> bool:
        """
        Equal operator for the Sell
        :param other: the other Sell
        :type other: Sell
        :return: True if the Sells are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Sell):
            return self.__id == other.id and \
                self.__date == other.date and \
                self.__pay_method == other.pay_method and \
                self.__total_price == other.total_price and \
                self.__items == other.items
        return False


if __name__ == '__main__':
    sell1 = Sell(1, date.today(), 'pay_method', 0.1, [Document().__str__()])

    print(sell1.__str__())

    sell2 = Sell(1, date.today(), 'pay_method', 0.1, [Document().__str__()])

    print("sell1 == sell2") if sell1 == sell2 else print("sell1 != sell2")
