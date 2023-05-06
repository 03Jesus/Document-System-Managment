from classes.edocument import EDocument
from datetime import date

class InvBook(EDocument):
    """
    A class that represents an investigation book
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
                 doi: str = 'doi',
                 pages: int = 1,
                 abstract: str = 'abstract') -> object:
        """
        Constructor of the class
        :param id: the id of the investigation book
        :type id: int
        :param author: the author of the investigation book
        :type author: str
        :param title: the title of the investigation book
        :type title: str
        :param price: the price of the investigation book
        :type price: float
        :param topic: the topic of the investigation book
        :type topic: str
        :param language: the language of the investigation book
        :type language: str
        :param pub_date: the publication date of the investigation book
        :type pub_date: date
        :param size: the size of the investigation book
        :type size: float
        :param doi: the doi of the investigation book
        :type doi: str
        :param pages: the number of pages of the investigation book
        :type pages: int
        :param abstract: the abstract of the investigation book
        :type abstract: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date, size, doi)
        self.__pages = pages
        self.__abstract = abstract

    @property
    def pages(self) -> int:
        """
        Getter for the number of pages of the investigation book
        :return: the number of pages of the investigation book
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int):
        """
        Setter for the number of pages of the investigation book
        :param pages: the number of pages of the investigation book
        :type pages: int
        """
        self.__pages = pages
    
    @property
    def abstract(self) -> str:
        """
        Getter for the abstract of the investigation book
        :return: the abstract of the investigation book
        :rtype: str
        """
        return self.__abstract
    
    @abstract.setter
    def abstract(self, abstract: str):
        """
        Setter for the abstract of the investigation book
        :param abstract: the abstract of the investigation book
        :type abstract: str
        """
        self.__abstract = abstract

    def __str__(self) -> str:
        """
        String representation of the investigation book
        :return: the string representation of the investigation book
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
                "doi": self.doi,
                "pages": self.pages,
                "abstract": self.abstract}
    
    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, InvBook):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date and \
                   self.size == other.size and \
                   self.doi == other.doi and \
                   self.pages == other.pages and \
                   self.abstract == other.abstract
        return False

if __name__ == "__main__":
    invbook = InvBook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 'abstract')
    assert invbook.id == 1
    assert invbook.author == 'author'
    assert invbook.title == 'title'
    assert invbook.price == 0.1
    assert invbook.topic == 'topic'
    assert invbook.language == 'lang'
    assert invbook.pub_date == date.today()
    assert invbook.size == 0.1
    assert invbook.doi == 'doi'
    assert invbook.pages == 1
    assert invbook.abstract == 'abstract'

    print(invbook.__str__())

    invbook2 = InvBook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 'abstract')

    print("invbook == invbook2") if invbook == invbook2 else print("invbook != invbook2")