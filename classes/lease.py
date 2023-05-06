import json
from datetime import date
from document import Document


class Lease(object):
    """
    A class that represents a Lease
    """

    def __init__(self,
                 id: int = 0,
                 start_date: date = date.today(),
                 finish_date: date = date(date.today().year,
                                          date.today().month+1,
                                          31),
                 pay_method: str = 'pay_method',
                 total_price: float = 0.1,
                 items: list = [Document()]) -> object:
        """
        Constructor of the class
        :param id: the id of the Lease
        :type id: int
        :param start_date: the start_date of the Lease
        :type start_date: date
        :param finish_date: the finish_date of the Lease
        :type finish_date: date
        :param pay_method: the pay_method of the Lease
        :type pay_method: str
        :param total_price: the total_price of the Lease
        :type total_price: float
        :param items: the items of the Lease
        :type items: list
        """
        self.__id = id
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__pay_method = pay_method
        self.__total_price = total_price
        self.__items = items

    @property
    def id(self) -> int:
        """
        Getter for the id of the Lease
        :return: the id of the Lease
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Lease
        :param id: the new id of the Lease
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def start_date(self) -> date:
        """
        Getter for the start_date of the Lease
        :return: the start_date of the Lease
        :rtype: date
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: date) -> None:
        """
        Setter for the start_date of the Lease
        :param start_date: the new start_date of the Lease
        :type start_date: date
        :return: None
        """
        self.__start_date = start_date

    @property
    def finish_date(self) -> date:
        """
        Getter for the finish_date of the Lease
        :return: the finish_date of the Lease
        :rtype: date
        """
        return self.__finish_date

    @finish_date.setter
    def finish_date(self, finish_date: date) -> None:
        """
        Setter for the finish_date of the Lease
        :param finish_date: the new finish_date of the Lease
        :type finish_date: date
        :return: None
        """
        self.__finish_date = finish_date

    @property
    def pay_method(self) -> str:
        """
        Getter for the pay_method of the Lease
        :return: the pay_method of the Lease
        :rtype: str
        """
        return self.__pay_method

    @pay_method.setter
    def pay_method(self, pay_method: str) -> None:
        """
        Setter for the pay_method of the Lease
        :param pay_method: the new pay_method of the Lease
        :type pay_method: str
        :return: None
        """
        self.__pay_method = pay_method

    @property
    def total_price(self) -> float:
        """
        Getter for the total_price of the Lease
        :return: the total_price of the Lease
        :rtype: float
        """
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float) -> None:
        """
        Setter for the total_price of the Lease
        :param total_price: the new total_price of the Lease
        :type total_price: float
        :return: None
        """
        self.__total_price = total_price

    @property
    def items(self) -> list:
        """
        Getter for the items of the Lease
        :return: the items of the Lease
        :rtype: list
        """
        return self.__items

    @items.setter
    def items(self, items: list) -> None:
        """
        Setter for the items of the Lease
        :param items: the new items of the Lease
        :type items: list
        :return: None
        """
        self.__items = items

    def __str__(self) -> str:
        """
        String representation of the Lease
        :return: the string representation of the Lease
        :rtype: str
        """
        return {"id": self.__id,
                "start_date": self.__start_date,
                "finish_date": self.__finish_date,
                "pay_method": self.__pay_method,
                "total_price": self.__total_price,
                "items": self.__items}

    def __eq__(self, other: object) -> bool:
        """
        Equal operator for the Lease
        :param other: the other Lease
        :type other: object
        :return: True if the Leases are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Lease):
            return self.__id == other.__id and \
                self.__start_date == other.__start_date and \
                self.__finish_date == other.__finish_date and \
                self.__pay_method == other.__pay_method and \
                self.__total_price == other.__total_price and \
                self.__items == other.__items
        return False


if __name__ == "__main__":
    doc1 = Document(1, "author", "doc1", 1.0, "fantasy", 'esp')

    lease1 = Lease(1,
                   date.today(),
                   date(date.today().year,
                        date.today().month+1,
                        31),
                   "cash",
                   1.0,
                   [doc1.__str__()])
    lease2 = Lease(1,
                   date.today(),
                   date(date.today().year,
                        date.today().month+1,
                        31),
                   "cash",
                   1.0,
                   [doc1.__str__()])

    print(lease1.__str__())

    print("Lease1 == Lease2") if lease1 == lease2 else print("Lease1 != Lease2")
