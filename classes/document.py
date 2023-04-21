class Document(object):
    """
    A class that represents a document
    """
    def __init__(self, id: int = 0, author: str = 'author',
                title: str = 'title', price: float = 0.1,
                topic: str = 'topic', language: str = 'esp') -> object:
        """
        Constructor of the class
        :param id: the id of the document
        :type id: int
        :param author: the author of the document
        :type author: str
        :param title: the title of the document
        :type title: str
        :param price: the price of the document
        :type price: float
        :param topi: the topic of the document
        :type topi: str
        :param language: the language of the document
        :type language: str
        """
        self.__id = id
        self.__author = author
        self.__title = title
        self.__price = price
        self.__topic = topic
        self.__language = language
    
    @property
    def id(self) -> int:
        """
        Getter of the id
        :return: the id of the document
        :rtype: int
        """
        return self.__id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Setter of the id
        :param id: the id of the document
        :type id: int
        """
        self.__id = id

    @property
    def author(self) -> str:
        """
        Getter of the author
        :return: the author of the document
        :rtype: str
        """
        return self.__author
    
    @author.setter
    def author(self, author: str) -> None:
        """
        Setter of the author
        :param author: the author of the document
        :type author: str
        """
        self.__author = author

    @property
    def title(self) -> str:
        """
        Getter of the title
        :return: the title of the document
        :rtype: str
        """
        return self.__title
    
    @title.setter
    def title(self, title: str) -> None:
        """
        Setter of the title
        :param title: the title of the document
        :type title: str
        """
        self.__title = title

    @property
    def price(self) -> float:
        """
        Getter of the price
        :return: the price of the document
        :rtype: float
        """
        return self.__price
    
    @price.setter
    def price(self, price: float) -> None:
        """
        Setter of the price
        :param price: the price of the document
        :type price: float
        """
        self.__price = price

    @property
    def topic(self) -> str:
        """
        Getter of the topic
        :return: the topic of the document
        :rtype: str
        """
        return self.__topic
    
    @topic.setter
    def topic(self, topic: str) -> None:
        """
        Setter of the topic
        :param topic: the topic of the document
        :type topic: str
        """
        self.__topic = topic

    @property
    def language(self) -> str:
        """
        Getter of the language
        :return: the language of the document
        :rtype: str
        """
        return self.__language
    
    @language.setter
    def language(self, language: str) -> None:
        """
        Setter of the language
        :param language: the language of the document
        :type language: str
        """
        self.__language = language
    
    def buy(self, quantity: int) -> float:
        """
        Method that calculates the total price of a document
        :param quantity: the quantity of documents
        :type quantity: int
        :return: the total price of the documents
        :rtype: float
        """
        return self.price * quantity

    def __str__(self) -> str:
        """
        Method that returns a string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        # return in JSON format
        return {"id": self.id, "author": self.author, "title": self.title, "price": self.price, "topic": self.topic, "language": self.language}

    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Document):
            return self.id == other.id and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language
        return False

if __name__ == '__main__':
    
    test_doc = Document(5, 'Gabriel García', '100 Años De Soledad', 299, 'Novel', 'esp')
    print(test_doc)