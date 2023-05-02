from classes.edoc import Edoc
from datetime import date

class AudioBook(Edoc):
    """
    A class that represents an audio book
    """
    def __init__(self, id: int = 0, author: str = 'author',
                title: str = 'title', price: float = 0.1,
                topic: str = 'topic', language: str = 'esp',
                pub_date: date = date.today(), size: float = 0.1, doi: str = 'doi',
                hours: int = 1, minutes: int = 1, seconds: int = 1, 
                synopsis: str = 'synopsis') -> object:
        """
        Constructor of the class
        :param id: the id of the audio book
        :type id: int
        :param author: the author of the audio book
        :type author: str
        :param title: the title of the audio book
        :type title: str
        :param price: the price of the audio book
        :type price: float
        :param topi: the topic of the audio book
        :type topi: str
        :param language: the language of the audio book
        :type language: str
        :param pub_date: the publication date of the audio book
        :type pub_date: str
        :param size: the size of the audio book
        :type size: float
        :param doi: the doi of the audio book
        :type doi: str
        :param hours: the hours of the audio book
        :type hours: int
        :param minutes: the minutes of the audio book
        :type minutes: int
        :param seconds: the seconds of the audio book
        :type seconds: int
        :param synopsis: the synopsis of the audio book
        :type synopsis: str
        """
        super().__init__(id, author, title, price, topic, language)
        self.__pub_date = pub_date
        self.__size = size
        self.__doi = doi
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__synopsis = synopsis

    @property
    def pub_date(self) -> date:
        """
        Getter of the publication date
        :return: the publication date of the audio book
        :rtype: date
        """
        return self.__pub_date
    
    @pub_date.setter
    def pub_date(self, pub_date: date) -> None:
        """
        Setter of the publication date
        :param pub_date: the publication date of the audio book
        :type pub_date: date
        """
        self.__pub_date = pub_date

    @property
    def size(self) -> float:
        """
        Getter of the size
        :return: the size of the audio book
        :rtype: float
        """
        return self.__size
    
    @size.setter
    def size(self, size: float) -> None:
        """
        Setter of the size
        :param size: the size of the audio book
        :type size: float
        """
        self.__size = size

    @property
    def doi(self) -> str:
        """
        Getter of the doi
        :return: the doi of the audio book
        :rtype: str
        """
        return self.__doi
    
    @doi.setter
    def doi(self, doi: str) -> None:
        """
        Setter of the doi
        :param doi: the doi of the audio book
        :type doi: str
        """
        self.__doi = doi

    @property
    def hours(self) -> int:
        """
        Getter of the hours
        :return: the hours of the audio book
        :rtype: int
        """
        return self.__hours
    
    @hours.setter
    def hours(self, hours: int) -> None:
        """
        Setter of the hours
        :param hours: the hours of the audio book
        :type hours: int
        """
        self.__hours = hours

    @property
    def minutes(self) -> int:
        """
        Getter of the minutes
        :return: the minutes of the audio book
        :rtype: int
        """
        return self.__minutes
    
    @minutes.setter
    def minutes(self, minutes: int) -> None:
        """
        Setter of the minutes
        :param minutes: the minutes of the audio book
        :type minutes: int
        """
        self.__minutes = minutes

    @property
    def seconds(self) -> int:
        """
        Getter of the seconds
        :return: the seconds of the audio book
        :rtype: int
        """
        return self.__seconds
    
    @seconds.setter
    def seconds(self, seconds: int) -> None:
        """
        Setter of the seconds
        :param seconds: the seconds of the audio book
        :type seconds: int
        """
        self.__seconds = seconds

    @property
    def synopsis(self) -> str:
        """
        Getter of the synopsis
        :return: the synopsis of the audio book
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter of the synopsis
        :param synopsis: the synopsis of the audio book
        :type synopsis: str
        """
        self.__synopsis = synopsis

    def __str__(self) -> str:
        """
        String representation of the class
        :return: the string representation of the class
        :rtype: str
        """
        #return in JSON format
        return {"id": self.id, "author": self.author, "title": self.title, "price": self.price, "topic": self.topic, "language": self.language, "pub_date": self.pub_date, "size": self.size, "doi": self.doi, "hours": self.hours, "minutes": self.minutes, "seconds": self.seconds, "synopsis": self.synopsis}    
    
    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, AudioBook):
            return self.id == other.id and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language and self.pub_date == other.pub_date and self.size == other.size and self.doi == other.doi and self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds and self.synopsis == other.synopsis
        return False