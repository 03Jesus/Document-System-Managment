from classes.person import Person

class Client(Person):
    """
    Class that represents a client
    """
    
    def __init__(self, id: int = 0, name: str = 'name', 
                last_name: str = 'last_name', phone: str = 'phone',
                mail: str = 'mail') -> object:
        """
        Constructor of the class
        :param id: the id of the client
        :type id: int
        :param name: the name of the client
        :type name: str
        :param last_name: the last name of the client
        :type last_name: str
        :param phone: the phone of the client
        :type phone: str
        :param mail: the mail of the client
        :type mail: str
        """
        super().__init__(id, name, last_name, phone, mail)

    def buyHistory(self) -> list:
        """
        Method that returns the buy history of the client
        :return: the buy history of the client
        :rtype: list
        """
        pass

    def leaseHistory(self) -> list:
        """
        Method that returns the lease history of the client
        :return: the lease history of the client
        :rtype: list
        """
        pass

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return (f'***Printing Client {self.id} ***'
                f'\nClient ID: {self.id} \nClient name: {self.name} \nClient last name: {self.last_name}' 
                f'\nClient phone: {self.phone} \nClient mail: {self.mail}\n')

    def __eq__(self, other: object) -> bool:
        """
        Method that returns if two objects are equal
        :param other: the other object
        :type other: object
        :return: if the objects are equal
        :rtype: bool
        """
        return super().__eq__(other)