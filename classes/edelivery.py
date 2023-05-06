from datetime import date
import json
from delivery import Delivery
from person import Person

class EDelivery (Delivery):
    """
    A class that represents an Electronic Delivery
    """
    def __init__(self,
                 id: int = 0,
                 buyer: Person = Person(),
                 date: date = date.today(),
                 deliver_mail: str = 'deliver_mail') -> object:
        """
        Constructor of the class
        :param id: the id of the Delivery
        :type id: int
        :param buyer: the buyer of the Delivery
        :type buyer: Person
        :param date: the date of the Delivery
        :type date: str
        :param deliver_mail: the deliver mail of the Delivery
        :type deliver_mail: str
        """
        super().__init__(id, buyer, date)
        self.__deliver_mail = deliver_mail

    @property
    def deliver_mail(self) -> str:
        """
        Getter for the deliver mail of the Delivery
        :return: the deliver mail of the Delivery
        :rtype: str
        """
        return self.__deliver_mail
    
    @deliver_mail.setter
    def deliver_mail(self, deliver_mail: str) -> None:
        """
        Setter for the deliver mail of the Delivery
        :param deliver_mail: the new deliver mail of the Delivery
        :type deliver_mail: str
        :return: None
        """
        self.__deliver_mail = deliver_mail

    def __str__(self) -> str:
        """
        String representation of the class
        :return: a string representing the class
        :rtype: str
        """
        return {"id": self.id,
                "buyer": self.buyer,
                "date": self.date,
                "deliver_mail": self.deliver_mail}
    
    def __eq__(self, other: object) -> bool:
        """
        Equals method
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, EDelivery):
            return self.id == other.id and \
                   self.buyer == other.buyer and \
                   self.date == other.date and \
                   self.deliver_mail == other.deliver_mail
        return False

if __name__ == '__main__':
    buyer = Person(1, 'name', 'last_name', 'phone', 'mail')
    edelivery = EDelivery(1, buyer.__str__(), date.today(), 'deliver_mail')
    print(edelivery.__str__())
    edelivery2 = EDelivery(1, buyer.__str__(), date.today(), 'deliver_mail')

    print("edeliver1 == edelivery2") if edelivery.__eq__(edelivery2) else print("edeliver1 != edelivery2")