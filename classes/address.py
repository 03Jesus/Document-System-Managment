import json


class Address (object):
    """
    Class for the address of a person
    """

    def __init__(self,
                 country: str = 'country',
                 department: str = 'department',
                 city: str = 'str',
                 post_code: str = 'post_code',
                 neighborhood: str = 'neighborhood',
                 street: str = 'street',
                 complement: str = 'complement') -> object:
        """
        Constructor of the class
        :param country: the country of the address
        :type country: str
        :param department: the department of the address
        :type department: str
        :param city: the city of the address
        :type city: str
        :param post_code: the post code of the address
        :type post_code: str
        :param neighborhood: the neighborhood of the address
        :type neighborhood: str
        :param street: the street of the address
        :type street: str
        :param complement: the complement of the address
        :type complement: str
        """
        self.__country = country
        self.__department = department
        self.__city = city
        self.__post_code = post_code
        self.__neighborhood = neighborhood
        self.__street = street
        self.__complement = complement

    @property
    def country(self) -> str:
        """
        Getter for the country of the address
        :return: the country of the address
        :rtype: str
        """
        return self.__country

    @country.setter
    def country(self, country: str) -> None:
        """
        Setter for the country of the address
        :param country: the new country of the address
        :type country: str
        :return: None
        """
        self.__country = country

    @property
    def department(self) -> str:
        """
        Getter for the department of the address
        :return: the department of the address
        :rtype: str
        """
        return self.__department

    @department.setter
    def department(self, department: str) -> None:
        """
        Setter for the department of the address
        :param department: the new department of the address
        :type department: str
        :return: None
        """
        self.__department = department

    @property
    def city(self) -> str:
        """
        Getter for the city of the address
        :return: the city of the address
        :rtype: str
        """
        return self.__city

    @city.setter
    def city(self, city: str) -> None:
        """
        Setter for the city of the address
        :param city: the new city of the address
        :type city: str
        :return: None
        """
        self.__city = city

    @property
    def post_code(self) -> str:
        """
        Getter for the post code of the address
        :return: the post code of the address
        :rtype: str
        """
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code: str) -> None:
        """
        Setter for the post code of the address
        :param post_code: the new post code of the address
        :type post_code: str
        :return: None
        """
        self.__post_code = post_code

    @property
    def neighborhood(self) -> str:
        """
        Getter for the neighborhood of the address
        :return: the neighborhood of the address
        :rtype: str
        """
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str) -> None:
        """
        Setter for the neighborhood of the address
        :param neighborhood: the new neighborhood of the address
        :type neighborhood: str
        :return: None
        """
        self.__neighborhood = neighborhood

    @property
    def street(self) -> str:
        """
        Getter for the street of the address
        :return: the street of the address
        :rtype: str
        """
        return self.__street

    @street.setter
    def street(self, street: str) -> None:
        """
        Setter for the street of the address
        :param street: the new street of the address
        :type street: str
        :return: None
        """
        self.__street = street

    @property
    def complement(self) -> str:
        """
        Getter for the complement of the address
        :return: the complement of the address
        :rtype: str
        """
        return self.__complement

    @complement.setter
    def complement(self, complement: str) -> None:
        """
        Setter for the complement of the address
        :param complement: the new complement of the address
        :type complement: str
        :return: None
        """
        self.__complement = complement

    def __str__(self) -> str:
        """
        String representation of the address
        :return: the string representation of the address
        :rtype: str
        """
        return {"country": self.__country,
                "department": self.__department,
                "city": self.__city,
                "post_code": self.__post_code,
                "neighborhood": self.__neighborhood,
                "street": self.__street,
                "complement": self.__complement}

    def __eq__(self, other) -> bool:
        """
        Equality operator for the address
        :param other: the other address
        :type other: Address
        :return: True if the addresses are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Address):
            return self.__country == other.country and \
                self.__department == other.department and \
                self.__city == other.city and \
                self.__post_code == other.post_code and \
                self.__neighborhood == other.neighborhood and \
                self.__street == other.street and \
                self.__complement == other.complement
        return False


if __name__ == '__main__':
    address1 = Address("country1", "department1",
                       "city1", "post_code1",
                       "neighborhood1", "street1",
                       "complement1")
    address2 = Address("country2", "department2",
                       "city2", "post_code2",
                       "neighborhood2", "street2",
                       "complement2")
    assert address1.country == "country1"

    print(address1.__str__())

    print("Addresses are equal") if address1 == address2 else print(
        "Addresses are not equal")
