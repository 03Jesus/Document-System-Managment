import json
from classes.document import Document
from datetime import date

class EDocument(Document):
    """
    A class that represents an electronic document
    """
    def __init__(self,
                 id: int = 0,
                 author: str = 'author',
                 title: str = 'title',
                 price: float = 0.1,
                 topic: str = 'topic',
                 language: str = 'lang',
                 pub_date: date = date.today(),
                 size: float = 0.1,
                 doi: str = 'doi') -> object:
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
        :param pub_date: the publication date of the document
        :type pub_date: date
        :param size: the size of the document
        :type size: float
        :param doi: the doi of the document
        :type doi: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date)
        self.__size = size
        self.__doi = doi

    @property
    def size(self) -> float:
        """
        Getter for the size of the document
        :return: the size of the document
        :rtype: float
        """
        return self.__size
    
    @size.setter
    def size(self, size: float) -> None:
        """
        Setter for the size of the document
        :param size: the new size of the document
        :type size: float
        :return: None
        """
        self.__size = size

    @property
    def doi(self) -> str:
        """
        Getter for the doi of the document
        :return: the doi of the document
        :rtype: str
        """
        return self.__doi
    
    @doi.setter
    def doi(self, doi: str) -> None:
        """
        Setter for the doi of the document
        :param doi: the new doi of the document
        :type doi: str
        :return: None
        """
        self.__doi = doi

    def __str__(self) -> str:
        """
        String representation of the class
        :return: the string representation of the class
        :rtype: str
        """
        return {"id": self.id,
                "author": self.author,
                "title": self.title,
                "price": self.price,
                "topic": self.topic,
                "language": self.language,
                "pub_date": self.pub_date.strftime("%Y/%m/%d"),
                "size": self.size,
                "doi": self.doi}
    
    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, EDocument):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date and \
                   self.size == other.size and \
                   self.doi == other.doi
        return False
        
if __name__ == "__main__":
    edocument = EDocument(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi')
    assert edocument.id == 1
    assert edocument.author == 'author'
    assert edocument.title == 'title'
    assert edocument.price == 0.1
    assert edocument.topic == 'topic'
    assert edocument.language == 'lang'
    assert edocument.pub_date == date.today()
    assert edocument.size == 0.1
    assert edocument.doi == 'doi'

    print(json.dumps(edocument.__str__()))

    edocument2 = EDocument(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi')

    print("edocument == edocument2") if edocument == edocument2 else print("edocument != edocument2")
        