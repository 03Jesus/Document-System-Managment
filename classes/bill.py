import json
from person import Person
from document import Document
from datetime import date


class Bill (object):
    """
    A class that represents a Bill
    """

    def __init__(self,
                 id: int = 0,
                 buyer: Person = Person(),
                 date: date = date.today(),
                 price: float = 0.1,
                 items: list = [Document()]) -> object:
        """
        Constructor of the class
        :param id: the id of the Bill
        :type id: int
        :param buyer: the buyer of the Bill
        :type buyer: Person
        :param date: the date of the Bill
        :type date: str
        :param price: the price of the Bill
        :type price: float
        :param items: the items of the Bill
        :type items: list
        """
        self.__id = id
        self.__buyer = buyer
        self.__date = date
        self.__price = price
        self.__items = items

    @property
    def id(self) -> int:
        """
        Getter for the id of the Bill
        :return: the id of the Bill
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Bill
        :param id: the new id of the Bill
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def buyer(self) -> Person:
        """
        Getter for the buyer of the Bill
        :return: the buyer of the Bill
        :rtype: Person
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, buyer: Person) -> None:
        """
        Setter for the buyer of the Bill
        :param buyer: the new buyer of the Bill
        :type buyer: Person
        :return: None
        """
        self.__buyer = buyer

    @property
    def date(self) -> date:
        """
        Getter for the date of the Bill
        :return: the date of the Bill
        :rtype: date
        """
        return self.__date

    @date.setter
    def date(self, date: date) -> None:
        """
        Setter for the date of the Bill
        :param date: the new date of the Bill
        :type date: date
        :return: None
        """
        self.__date = date

    @property
    def price(self) -> float:
        """
        Getter for the price of the Bill
        :return: the price of the Bill
        :rtype: float
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """
        Setter for the price of the Bill
        :param price: the new price of the Bill
        :type price: float
        :return: None
        """
        self.__price = price

    @property
    def items(self) -> list:
        """
        Getter for the items of the Bill
        :return: the items of the Bill
        :rtype: list
        """
        return self.__items

    @items.setter
    def items(self, items: list) -> None:
        """
        Setter for the items of the Bill
        :param items: the new items of the Bill
        :type items: list
        :return: None
        """
        self.__items = items

    def __str__(self) -> str:
        """
        String representation of the Bill
        :return: the string representation of the Bill
        :rtype: str
        """
        return {"id": self.__id,
                "buyer": self.__buyer,
                "date": self.__date,
                "price": self.__price,
                "items": self.__items}

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Bills are equal
        :param other: the other Bill
        :type other: object
        :return: True if the Bills are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Bill):
            return self.__id == other.id and \
                self.__buyer == other.buyer and \
                self.__date == other.date and \
                self.__price == other.price and \
                self.__items == other.items
        return False


if __name__ == "__main__":
    person = Person(1, "John", "Doe", "1234567890123", "JohnDoe@johndoe.com")
    doc1 = Document(1, "author", "doc1", 1.0, "fantasy", 'esp')
    doc2 = Document(2, "author", "doc2", 2.0, "fantasy", 'esp')

    bill1 = Bill(1, person.__str__(), date.today(),
                 3.0, [doc1.__str__(), doc2.__str__()])
    bill2 = Bill(1, person.__str__(), date.today(),
                 3.0, [doc1.__str__(), doc2.__str__()])

    print(bill1.__str__())

    print("Bill1 == Bill2") if bill1 == bill2 else print("Bill1 != Bill2")
