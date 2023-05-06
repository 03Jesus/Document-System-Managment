import json
from person import Person
from address import Address
from document import Document


class Provider (Person):
    """
    A class that represents a Provider
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 last_name: str = 'last_name',
                 phone: str = 'phone',
                 mail: str = 'mail',
                 address: Address = Address(),
                 inventory: list = [Document()]) -> object:
        """
        Constructor of the class
        :param id: the id of the Provider
        :type id: int
        :param name: the name of the Provider
        :type name: str
        :param last_name: the last name of the Provider
        :type last_name: str
        :param phone: the phone of the Provider
        :type phone: str
        :param mail: the mail of the Provider
        :type mail: str
        :param address: the address of the Provider
        :type address: Address
        :param inventory: the inventory of the Provider
        :type inventory: list
        """
        super().__init__(id, name, last_name, phone, mail)
        self.__address = address
        self.__inventory = inventory

    @property
    def address(self) -> Address:
        """
        Getter for the address of the Provider
        :return: the address of the Provider
        :rtype: Address
        """
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        """
        Setter for the address of the Provider
        :param address: the new address of the Provider
        :type address: Address
        :return: None
        """
        self.__address = address

    @property
    def inventory(self) -> list:
        """
        Getter for the inventory of the Provider
        :return: the inventory of the Provider
        :rtype: list
        """
        return self.__inventory

    @inventory.setter
    def inventory(self, inventory: list) -> None:
        """
        Setter for the inventory of the Provider
        :param inventory: the new inventory of the Provider
        :type inventory: list
        :return: None
        """
        self.__inventory = inventory

    def __str__(self) -> str:
        """
        Method that returns the string representation of the Provider
        :return: the string representation of the Provider
        :rtype: str
        """
        return {"id": self.id,
                "name": self.name,
                "last_name": self.last_name,
                "phone": self.phone,
                "mail": self.mail,
                "address": self.address,
                "inventory": self.inventory}

    def __eq__(self, other: object) -> bool:
        """
        Method that checks if two Providers are equal
        :param other: the other Provider
        :type other: object
        :return: True if the Providers are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Provider):
            return self.id == other.id and \
                self.name == other.name and \
                self.last_name == other.last_name and \
                self.phone == other.phone and \
                self.mail == other.mail and \
                self.address == other.address and \
                self.inventory == other.inventory
        return False


if __name__ == '__main__':
    provider = Provider(1,
                        'name',
                        'last_name',
                        'phone',
                        'mail',
                        Address().__str__(),
                        [Document().__str__()])
    assert provider.id == 1

    print(json.dumps(provider.__str__()))

    provider2 = Provider(1, 'name', 'last_name', 'phone',
                         'mail', Address(), [Document()])

    if provider == provider2:
        print('provider1 == provider2')
    else:
        print('provider1 != provider2')
