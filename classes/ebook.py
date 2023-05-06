from classes.edocument import EDocument
from datetime import date

class Ebook(EDocument):
    """
    A class that represents an ebook
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
                 editor: str = 'editor',
                 pages: int = 1,
                 synopsis: str = 'synopsis') -> object:
        """
        Constructor of the class
        :param id: the id of the Ebook
        :type id: int
        :param author: the author of the Ebook
        :type author: str
        :param title: the title of the Ebook
        :type title: str
        :param price: the price of the Ebook
        :type price: float
        :param topic: the topic of the Ebook
        :type topic: str
        :param language: the language of the Ebook
        :type language: str
        :param pub_date: the publication date of the Ebook
        :type pub_date: date
        :param size: the size of the Ebook
        :type size: float
        :param doi: the doi of the Ebook
        :type doi: str
        :param editor: the editor of the Ebook
        :type editor: str
        :param pages: the number of pages of the Ebook
        :type pages: int
        :param synopsis: the synopsis of the Ebook
        :type synopsis: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date, size, doi)
        self.__editor = editor
        self.__pages = pages
        self.__synopsis = synopsis

    @property
    def editor(self) -> str:
        """
        Getter for the editor of the Ebook
        :return: the editor of the Ebook
        :rtype: str
        """
        return self.__editor
    
    @editor.setter
    def editor(self, editor: str) -> None:
        """
        Setter for the editor of the Ebook
        :param editor: the editor of the Ebook
        :type editor: str
        """
        self.__editor = editor

    @property
    def pages(self) -> int:
        """
        Getter for the number of pages of the Ebook
        :return: the number of pages of the Ebook
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter for the number of pages of the Ebook
        :param pages: the number of pages of the Ebook
        :type pages: int
        """
        self.__pages = pages

    @property
    def synopsis(self) -> str:
        """
        Getter for the synopsis of the Ebook
        :return: the synopsis of the Ebook
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter for the synopsis of the Ebook
        :param synopsis: the synopsis of the Ebook
        :type synopsis: str
        """
        self.__synopsis = synopsis

    def __str__(self) -> str:
        """
        String representation of the Ebook
        :return: the string representation of the Ebook
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
                "editor": self.editor,
                "pages": self.pages,
                "synopsis": self.synopsis}

    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Ebook):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date and \
                   self.size == other.size and \
                   self.doi == other.doi and \
                   self.editor == other.editor and \
                   self.pages == other.pages and \
                   self.synopsis == other.synopsis
        return False

if __name__ == "__main__":
    ebook = Ebook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 'editor', 1, 'synopsis')
    assert ebook.id == 1
    assert ebook.author == 'author'
    assert ebook.title == 'title'
    assert ebook.price == 0.1
    assert ebook.topic == 'topic'
    assert ebook.language == 'lang'
    assert ebook.pub_date == date.today()
    assert ebook.size == 0.1
    assert ebook.doi == 'doi'
    assert ebook.editor == 'editor'
    assert ebook.pages == 1
    assert ebook.synopsis == 'synopsis'

    print(ebook.__str__())

    ebook2 = Ebook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 'editor', 1, 'synopsis')

    print("ebook == ebook2") if ebook == ebook2 else print("ebook != ebook2")