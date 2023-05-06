import json
from datetime import date
class Document(object):
    """
    A class that represents a document
    """
    def __init__(self,
                 id: int = 0,
                 author: str = 'author',
                 title: str = 'title',
                 price: float = 0.1,
                 topic: str = 'topic',
                 language: str = 'lang',
                 pub_date: date = date.today()) -> object:
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
        :param topic: the topic of the document
        :type topic: str
        :param language: the language of the document
        :type language: str
        """

        self.__id = id
        self.__author = author
        self.__title = title
        self.__price = price
        self.__topic = topic
        self.__language = language
        self.__pub_date = pub_date

    @property
    def id(self) -> int:
        """
        Getter for the id of the document
        :return: the id of the document
        :rtype: int
        """
        return self.__id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Setter for the id of the document
        :param id: the new id of the document
        :type id: int
        :return: None
        """
        self.__id = id

    @property
    def author(self) -> str:
        """
        Getter for the author of the document
        :return: the author of the document
        :rtype: str
        """
        return self.__author
    
    @author.setter
    def author(self, author: str) -> None:
        """
        Setter for the author of the document
        :param author: the new author of the document
        :type author: str
        :return: None
        """
        self.__author = author

    @property
    def title(self) -> str:
        """
        Getter for the title of the document
        :return: the title of the document
        :rtype: str
        """
        return self.__title
    
    @title.setter
    def title(self, title: str) -> None:
        """
        Setter for the title of the document
        :param title: the new title of the document
        :type title: str
        :return: None
        """
        self.__title = title

    @property
    def price(self) -> float:
        """
        Getter for the price of the document
        :return: the price of the document
        :rtype: float
        """
        return self.__price
    
    @price.setter
    def price(self, price: float) -> None:
        """
        Setter for the price of the document
        :param price: the new price of the document
        :type price: float
        :return: None
        """
        self.__price = price

    @property
    def topic(self) -> str:
        """
        Getter for the topic of the document
        :return: the topic of the document
        :rtype: str
        """
        return self.__topic
    
    @topic.setter
    def topic(self, topic: str) -> None:
        """
        Setter for the topic of the document
        :param topic: the new topic of the document
        :type topic: str
        :return: None
        """
        self.__topic = topic

    @property
    def language(self) -> str:
        """
        Getter for the language of the document
        :return: the language of the document
        :rtype: str
        """
        return self.__language
    
    @language.setter
    def language(self, language: str) -> None:
        """
        Setter for the language of the document
        :param language: the new language of the document
        :type language: str
        :return: None
        """
        self.__language = language

    @property
    def pub_date(self) -> date:
        """
        Getter for the publication date of the document
        :return: the publication date of the document
        :rtype: date
        """
        return self.__pub_date
    
    @pub_date.setter
    def pub_date(self, pub_date: date) -> None:
        """
        Setter for the publication date of the document
        :param pub_date: the new publication date of the document
        :type pub_date: date
        :return: None
        """
        self.__pub_date = pub_date

    def __str__(self) -> str:
        """
        String representation of the document
        :return: the string representation of the document
        :rtype: str
        """
        return {"id": self.__id,
                "author": self.__author,
                "title": self.__title,
                "price": self.__price,
                "topic": self.__topic,
                "language": self.__language,
                "pub_date": self.__pub_date.strftime("%Y/%m/%d")}
    
    def __eq__(self, other: object) -> bool:
        """
        Overriding the equality operator
        :param other: the other document to compare to
        :type other: Document
        :return: True if the documents are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Document):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date
        return False
    
if __name__ == '__main__':
    doc = Document(1, 'author', 'title', 0.1, 'topic', 'lang', date.today())
    assert doc.id == 1
    assert doc.author == 'author'
    assert doc.title == 'title'
    assert doc.price == 0.1
    assert doc.topic == 'topic'
    assert doc.language == 'lang'
    assert doc.pub_date == date.today()

    doc2 = Document(2, 'author2', 'title2', 0.2, 'topic2', 'lang2', date.today())
    doc3 = Document(1, 'author', 'title', 0.1, 'topic', 'lang', date.today())
    print(doc.__str__())

    print("The documents are equal") if doc.__eq__(doc2) else print("The documents are not equal")
        