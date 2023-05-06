import json
from datetime import date
from delivery import Delivery
from person import Person
from address import Address


class PDelivery (Delivery):
    """
    A class that represents an Phisic Delivery
    """

    def __init__(self,
                 id: int = 0,
                 buyer: Person = Person(),
                 date: date = date.today(),
                 address: Address = Address(),
                 contact: Person = Person(),
                 company: str = 'company') -> object:
        """
        Constructor of the class
        :param id: the id of the Delivery
        :type id: int
        :param buyer: the buyer of the Delivery
        :type buyer: Person
        :param date: the date of the Delivery
        :type date: str
        :param address: the address of the Delivery
        :type address: Address
        :param contact: the contact of the Delivery
        :type contact: Person
        :param company: the company of the Delivery
        :type company: str
        """
        super().__init__(id, buyer, date)
        self.__address = address
        self.__contact = contact
        self.__company = company

    @property
    def address(self) -> Address:
        """
        Getter for the address of the Delivery
        :return: the address of the Delivery
        :rtype: Address
        """
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        """
        Setter for the address of the Delivery
        :param address: the new address of the Delivery
        :type address: Address
        :return: None
        """
        self.__address = address

    @property
    def contact(self) -> Person:
        """
        Getter for the contact of the Delivery
        :return: the contact of the Delivery
        :rtype: Person
        """
        return self.__contact

    @contact.setter
    def contact(self, contact: Person) -> None:
        """
        Setter for the contact of the Delivery
        :param contact: the new contact of the Delivery
        :type contact: Person
        :return: None
        """
        self.__contact = contact

    @property
    def company(self) -> str:
        """
        Getter for the company of the Delivery
        :return: the company of the Delivery
        :rtype: str
        """
        return self.__company

    @company.setter
    def company(self, company: str) -> None:
        """
        Setter for the company of the Delivery
        :param company: the new company of the Delivery
        :type company: str
        :return: None
        """
        self.__company = company

    def __str__(self) -> str:
        """
        String representation of the class
        :return: a string representing the class
        :rtype: str
        """
        return {"id": self.id,
                "buyer": self.buyer,
                "date": self.date,
                "address": self.address,
                "contact": self.contact,
                "company": self.company}

    def __eq__(self, other: object) -> bool:
        """
        Equality comparison between two instances of the class
        :param other: the other instance of the class
        :type other: object
        :return: True if the instances are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, PDelivery):
            return self.id == other.id and \
                self.buyer == other.buyer and \
                self.date == other.date and \
                self.address == other.address and \
                self.contact == other.contact and \
                self.company == other.company
        return False


if __name__ == '__main__':
    buyer = Person(1, 'name', 'surname', 'email', 'phone')
    address = Address(1, 'street', 'city', 'state', 'zip_code')
    contact = Person(1, 'name', 'surname', 'email', 'phone')

    phisic_delivery = PDelivery(1,
                                buyer.__str__(),
                                date.today(),
                                address.__str__(),
                                contact.__str__(),
                                'company')

    print(phisic_delivery.__str__())

    phisic_delivery2 = PDelivery(1,
                                 buyer.__str__(),
                                 date.today(),
                                 address.__str__(),
                                 contact.__str__(),
                                 'company')

    print("phisic_delivery == phisic_delivery2: ") if phisic_delivery == phisic_delivery2 else print(
        "phisic_delivery != phisic_delivery2: ")
