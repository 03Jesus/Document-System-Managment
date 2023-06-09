from classes.person import Person

class Administrator(Person):
    """
    Class that represents an administrator
    """

    def __init__(self, id: int = 0, name: str = 'name', 
                last_name: str = 'last_name', phone: str = 'phone',
                mail: str = 'mail') -> object:
        """
        Constructor of the class
        :param id: the id of the administrator
        :type id: int
        :param name: the name of the administrator
        :type name: str
        :param last_name: the last name of the administrator
        :type last_name: str
        :param phone: the phone of the administrator
        :type phone: str
        :param mail: the mail of the administrator
        :type mail: str
        """
        super().__init__(id, name, last_name, phone, mail)

    def addDocument(self) -> None:
        """
        Method that adds a document
        """
        pass

    def deleteDocument(self) -> None:
        """
        Method that deletes a document
        """
        pass

    def modifyDocument(self) -> None:
        """
        Method that modifies a document
        """
        pass

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return (f'***Printing Admin {self.id} ***'
                f'\nAdmin ID: {self.id} \nAdmin name: {self.name} \nAdmin last name: {self.last_name}' 
                f'\nAdmin phone: {self.phone} \nAdmin mail: {self.mail}\n')

    def __eq__(self, other: object) -> bool:
        """
        Method that returns if two objects are equal
        :param other: the other object
        :type other: object
        :return: if the objects are equal
        :rtype: bool
        """
        return super().__eq__(other)