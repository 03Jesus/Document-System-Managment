from classes.pdocument import PDocument
from datetime import date

class Book(PDocument):
    """
    A class that represents a book
    """

    def __init__(self,
                 id: int = 0,
                 author: str = 'author',
                 title: str = 'title',
                 price: float = 0.1,
                 topic: str = 'topic',
                 language: str = 'lang',
                 pub_date: date = date.today(),
                 publisher: str = 'publisher',
                 editor: str = 'editor',
                 pages: int = 1,
                 synopsis: str = 'synopsis',
                 presentation: str = 'presentation') -> object:
        """
        Constructor of the class
        :param id: the id of the book
        :type id: int
        :param author: the author of the book
        :type author: str
        :param title: the title of the book
        :type title: str
        :param price: the price of the book
        :type price: float
        :param topic: the topic of the book
        :type topic: str
        :param language: the language of the book
        :type language: str
        :param publisher: the publisher of the book
        :type publisher: str
        :param editor: the editor of the book
        :type editor: str
        :param pages: the number of pages of the book
        :type pages: int
        :param synopsis: the synopsis of the book
        :type synopsis: str
        :param presentation: the presentation of the book
        :type presentation: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date, publisher)
        self.__editor = editor
        self.__pages = pages
        self.__synopsis = synopsis
        self.__presentation = presentation

    @property
    def editor(self) -> str:
        """
        Getter for the editor of the book
        :return: the editor of the book
        :rtype: str
        """
        return self.__editor
    
    @editor.setter
    def editor(self, editor: str) -> None:
        """
        Setter for the editor of the book
        :param editor: the new editor of the book
        :type editor: str
        :return: None
        """
        self.__editor = editor

    @property
    def pages(self) -> int:
        """
        Getter for the number of pages of the book
        :return: the number of pages of the book
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter for the number of pages of the book
        :param pages: the new number of pages of the book
        :type pages: int
        :return: None
        """
        self.__pages = pages

    @property
    def synopsis(self) -> str:
        """
        Getter for the synopsis of the book
        :return: the synopsis of the book
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter for the synopsis of the book
        :param synopsis: the new synopsis of the book
        :type synopsis: str
        :return: None
        """
        self.__synopsis = synopsis

    @property
    def presentation(self) -> str:
        """
        Getter for the presentation of the book
        :return: the presentation of the book
        :rtype: str
        """
        return self.__presentation
    
    @presentation.setter
    def presentation(self, presentation: str) -> None:
        """
        Setter for the presentation of the book
        :param presentation: the new presentation of the book
        :type presentation: str
        :return: None
        """
        self.__presentation = presentation

    def __str__(self) -> str:
        """
        String representation of the book
        :return: the string representation of the book
        :rtype: str
        """
        return {"id": self.id,
                "author": self.author,
                "title": self.title,
                "price": self.price,
                "topic": self.topic,
                "language": self.language,
                "pub_date": self.pub_date.strftime("%Y/%m/%d"),
                "publisher": self.publisher,
                "editor": self.editor,
                "pages": self.pages,
                "synopsis": self.synopsis,
                "presentation": self.presentation}

    def __eq__(self, other) -> bool:
        """
        Checks if two documents are equal
        :param other: the other document
        :type other: Document
        :return: True if the documents are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Book):
            return self.id == other.id and \
                self.author == other.author and \
                self.title == other.title and \
                self.price == other.price and \
                self.topic == other.topic and \
                self.language == other.language and \
                self.pub_date == other.pub_date and \
                self.publisher == other.publisher and \
                self.editor == other.editor and \
                self.pages == other.pages and \
                self.synopsis == other.synopsis and \
                self.presentation == other.presentation
        return False

if __name__ == "__main__":
    book = Book(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 'publisher', 'editor', 1, 'synopsis', 'presentation')
    assert book.id == 1
    assert book.author == 'author'
    assert book.title == 'title'
    assert book.price == 0.1
    assert book.topic == 'topic'
    assert book.language == 'lang'
    assert book.pub_date == date.today()
    assert book.publisher == 'publisher'
    assert book.editor == 'editor'
    assert book.pages == 1
    assert book.synopsis == 'synopsis'
    assert book.presentation == 'presentation'

    print(book.__str__())

    book2 = Book(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 'publisher', 'editor', 1, 'synopsis', 'presentation')

    print("book == book2") if book == book2 else print("book != book2")