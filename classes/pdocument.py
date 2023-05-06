import json
from datetime import date
from classes.document import Document


class PDocument (Document):
    """
    A class that represents a physical document
    """

    def __init__(self,
                 id: int = 0,
                 author: str = 'author',
                 title: str = 'title',
                 price: float = 0.1,
                 topic: str = 'topic',
                 language: str = 'lang',
                 pub_date: date = date.today(),
                 publisher: str = 'publisher') -> object:
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
        :param publisher: the publisher of the document
        :type publisher: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date)
        self.__publisher = publisher

    @property
    def publisher(self) -> str:
        """
        Getter for the publisher of the document
        :return: the publisher of the document
        :rtype: str
        """
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str) -> None:
        """
        Setter for the publisher of the document
        :param publisher: the new publisher of the document
        :type publisher: str
        :return: None
        """
        self.__publisher = publisher

    def __str__(self) -> str:
        """
        String representation of the document
        :return: the string representation of the document
        :rtype: str
        """
        return {"id": self.id,
                "author": self.author,
                "title": self.title,
                "price": self.price,
                "topic": self.topic,
                "language": self.language,
                "pub_date": self.pub_date.strftime("%Y/%m/%d"),
                "publisher": self.publisher}

    def __eq__(self, other) -> bool:
        """
        Checks if two documents are equal
        :param other: the other document
        :type other: Document
        :return: True if the documents are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, PDocument):
            return self.id == other.id and \
                self.author == other.author and \
                self.title == other.title and \
                self.price == other.price and \
                self.topic == other.topic and \
                self.language == other.language and \
                self.pub_date == other.pub_date and \
                self.publisher == other.publisher
        return False


if __name__ == '__main__':
    doc = PDocument(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 'publisher')
    print(json.dumps(doc.__str__()))
    doc2 = PDocument(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 'publisher')
    print(doc == doc2)
