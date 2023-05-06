import json
from person import Person
from datetime import date


class Delivery (object):
    """
    A class that represents a Delivery
    """

    def __init__(self,
                 id: int = 0,
                 buyer: Person = Person(),
                 date: date = date.today()) -> object:
        """
        Constructor of the class
        :param id: the id of the Delivery
        :type id: int
        :param provider: the provider of the Delivery
        :type provider: Person
        :param date: the date of the Delivery
        :type date: str
        :param time: the time of the Delivery
        :type time: str
        :param status: the status of the Delivery
        :type status: str
        :param description: the description of the Delivery
        :type description: str
        """
        self.__id = id
        self.__buyer = buyer
        self.__date = date

    @property
    def id(self) -> int:
        """
        Getter for the id of the Delivery
        :return: the id of the Delivery
        :rtype: int
        """
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the Delivery
        :param id: the new id of the Delivery
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def buyer(self) -> Person:
        """
        Getter for the buyer of the Delivery
        :return: the buyer of the Delivery
        :rtype: Person
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, buyer: Person) -> None:
        """
        Setter for the buyer of the Delivery
        :param buyer: the new buyer of the Delivery
        :type buyer: Person
        :return: None
        """
        self.__buyer = buyer

    @property
    def date(self) -> date:
        """
        Getter for the date of the Delivery
        :return: the date of the Delivery
        :rtype: date
        """
        return self.__date

    @date.setter
    def date(self, date: date) -> None:
        """
        Setter for the date of the Delivery
        :param date: the new date of the Delivery
        :type date: date
        :return: None
        """
        self.__date = date

    def __str__(self) -> str:
        """
        String representation of the Delivery
        :return: the string representation of the Delivery
        :rtype: str
        """
        return {"id": self.__id,
                "buyer": self.__buyer,
                "date": self.__date}

    def __eq__(self, other: object) -> bool:
        """
        Equal operator for the Delivery
        :param other: the other Delivery
        :type other: Delivery
        :return: True if the Deliveries are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Delivery):
            return self.__id == other.id and \
                self.__buyer == other.buyer and \
                self.__date == other.date
        return False


if __name__ == '__main__':
    buyer = Person(1, 'name', 'last_name', 'phone', 'mail')
    delivery = Delivery(1, buyer.__str__(), date.today())
    print(delivery.__str__())
    delivery2 = Delivery(1, buyer.__str__(), date.today())

    if delivery == delivery2:
        print('delivery1 == delivery2')
    else:
        print('delivery1 != delivery2')
