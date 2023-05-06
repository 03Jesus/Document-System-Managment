from classes.edocument import EDocument
from datetime import date

class Magazine(EDocument):
    """
    A class that represents a magazine
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
                 edition: int = 1,
                 pages: int = 1) -> object:
        """
        Constructor of the class
        :param id: the id of the magazine
        :type id: int
        :param author: the author of the magazine
        :type author: str
        :param title: the title of the magazine
        :type title: str
        :param price: the price of the magazine
        :type price: float
        :param topic: the topic of the magazine
        :type topic: str
        :param language: the language of the magazine
        :type language: str
        :param pub_date: the publication date of the magazine
        :type pub_date: date
        :param size: the size of the magazine
        :type size: float
        :param doi: the doi of the magazine
        :type doi: str
        :param edition: the edition of the magazine
        :type edition: int
        :param pages: the number of pages of the magazine
        :type pages: int
        """
        super().__init__(id, author, title, price, topic, language, pub_date, size, doi)
        self.__edition = edition
        self.__pages = pages

    @property
    def edition(self) -> int:
        """
        Getter for the edition of the magazine
        :return: the edition of the magazine
        :rtype: int
        """
        return self.__edition
    
    @edition.setter
    def edition(self, edition: int):
        """
        Setter for the edition of the magazine
        :param edition: the edition of the magazine
        :type edition: int
        """
        self.__edition = edition

    @property
    def pages(self) -> int:
        """
        Getter for the number of pages of the magazine
        :return: the number of pages of the magazine
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int):
        """
        Setter for the number of pages of the magazine
        :param pages: the number of pages of the magazine
        :type pages: int
        """
        self.__pages = pages

    def __str__(self) -> str:
        """
        String representation of the magazine
        :return: the string representation of the magazine
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
                "edition": self.edition,
                "pages": self.pages}

    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Magazine):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date and \
                   self.size == other.size and \
                   self.doi == other.doi and \
                   self.edition == other.edition and \
                   self.pages == other.pages
        return False
    
if __name__ == "__main__":
    magazine = Magazine(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 1)
    assert magazine.id == 1
    assert magazine.author == 'author'
    assert magazine.title == 'title'
    assert magazine.price == 0.1
    assert magazine.topic == 'topic'
    assert magazine.language == 'lang'
    assert magazine.pub_date == date.today()
    assert magazine.size == 0.1
    assert magazine.doi == 'doi'
    assert magazine.edition == 1
    assert magazine.pages == 1
    
    
    print(magazine.__str__())

    magazine2 = Magazine(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 1)

    print("magazine == magazine2") if magazine == magazine2 else print("magazine != magazine2")