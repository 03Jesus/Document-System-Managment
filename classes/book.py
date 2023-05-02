from classes.fdoc import Fdoc

class Book(Fdoc):
    def __init__(self, id: int = '0', author: str = 'author',
                title: str = 'title', price: float = 0.1,
                topic: str = 'topic', language: str = 'esp',
                publisher: str = 'publisher', editor: str = 'edithor',
                pages: int = '1', synopsis: str = 'synopsis',
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
        :param topi: the topic of the book
        :type topi: str
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
        super().__init__(id, author, title, price, topic, language)
        self.publisher = publisher
        self.__editor = editor
        self.__pages = pages
        self.__synopsis = synopsis
        self.__presentation = presentation

    @property
    def publisher(self) -> str:
        """
        Getter of the publisher
        :return: the publisher of the book
        :rtype: str
        """
        return self.__publisher
    
    @publisher.setter
    def publisher(self, publisher: str) -> None:
        """
        Setter of the publisher
        :param publisher: the publisher of the book
        :type publisher: str
        """
        self.__publisher = publisher

    @property
    def editor(self) -> str:
        """
        Getter of the editor
        :return: the editor of the book
        :rtype: str
        """
        return self.__editor
    
    @editor.setter
    def editor(self, editor: str) -> None:
        """
        Setter of the editor
        :param editor: the editor of the book
        :type editor: str
        """
        self.__editor = editor

    @property
    def pages(self) -> int:
        """
        Getter of the number of pages
        :return: the number of pages of the book
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter of the number of pages
        :param pages: the number of pages of the book
        :type pages: int
        """
        self.__pages = pages

    @property
    def synopsis(self) -> str:
        """
        Getter of the synopsis
        :return: the synopsis of the book
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter of the synopsis
        :param synopsis: the synopsis of the book
        :type synopsis: str
        """
        self.__synopsis = synopsis

    @property
    def presentation(self) -> str:
        """
        Getter of the presentation
        :return: the presentation of the book
        :rtype: str
        """
        return self.__presentation
    
    @presentation.setter
    def presentation(self, presentation: str) -> None:
        """
        Setter of the presentation
        :param presentation: the presentation of the book
        :type presentation: str
        """
        self.__presentation = presentation

    def __str__(self) -> str:
        """
        Method to print the book
        :return: the book
        :rtype: str
        """
        #return in JSON format
        return{
        "id": self.id,
        "author": self.author, 
        "title": self.title, 
        "price": self.price, 
        "topic": self.topic, 
        "language": self.language, 
        "publisher": self.publisher, 
        "editor": self.editor, 
        "pages": self.pages, 
        "synopsis": self.synopsis, 
        "presentation": self.presentation
        }    
    
    def __eq__ (self, other: object) -> bool:
        """
        Method that returns True if the object is equal to other
        :param other: the other object
        :type other: object
        :return: True if the object is equal to other
        :rtype: bool
        """
        if isinstance(other, Book):
            return super().__eq__(other) and self.editor == other.editor and self.pages == other.pages and self.synopsis == other.synopsis and self.presentation == other.presentation
        return False