from classes.edocument import EDocument
from datetime import date

class AudioBook(EDocument):
    """
    A class that represents an audio book
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
                 duration: int = 1,
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
        :param topic: the topic of the audio book
        :type topic: str
        :param language: the language of the audio book
        :type language: str
        :param pub_date: the publication date of the audio book
        :type pub_date: date
        :param size: the size of the audio book
        :type size: float
        :param doi: the doi of the audio book
        :type doi: str
        :param duration: the duration of the audio book (in seconds)
        :type duration: int
        :param synopsis: the synopsis of the audio book
        :type synopsis: str
        """
        super().__init__(id, author, title, price, topic, language, pub_date, size, doi)
        self.__duration = duration
        self.__synopsis = synopsis

    @property
    def duration(self) -> int:
        """
        Getter for the duration of the audio book
        :return: the duration of the audio book
        :rtype: int
        """
        return self.__duration
    
    @duration.setter
    def duration(self, duration: int) -> None:
        """
        Setter for the duration of the audio book
        :param duration: the new duration of the audio book
        :type duration: int
        :return: None
        """
        self.__duration = duration

    @property
    def synopsis(self) -> str:
        """
        Getter for the synopsis of the audio book
        :return: the synopsis of the audio book
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter for the synopsis of the audio book
        :param synopsis: the new synopsis of the audio book
        :type synopsis: str
        :return: None
        """
        self.__synopsis = synopsis

    def __str__(self) -> str:
        """
        String representation of the audio book
        :return: the string representation of the audio book
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
                "duration": self.duration,
                "synopsis": self.synopsis}
    
    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, AudioBook):
            return self.id == other.id and \
                   self.author == other.author and \
                   self.title == other.title and \
                   self.price == other.price and \
                   self.topic == other.topic and \
                   self.language == other.language and \
                   self.pub_date == other.pub_date and \
                   self.size == other.size and \
                   self.doi == other.doi and \
                   self.duration == other.duration and \
                   self.synopsis == other.synopsis
        return False
    
if __name__ == "__main__":
    audio_book = AudioBook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 'synopsis')
    assert audio_book.id == 1
    assert audio_book.author == 'author'
    assert audio_book.title == 'title'
    assert audio_book.price == 0.1
    assert audio_book.topic == 'topic'
    assert audio_book.language == 'lang'
    assert audio_book.pub_date == date.today()
    assert audio_book.size == 0.1
    assert audio_book.doi == 'doi'
    assert audio_book.duration == 1
    assert audio_book.synopsis == 'synopsis'

    print(audio_book.__str__())

    audio_book2 = AudioBook(1, 'author', 'title', 0.1, 'topic', 'lang', date.today(), 0.1, 'doi', 1, 'synopsis')
    print("audio_book == audio_book2") if audio_book == audio_book2 else print("audio_book != audio_book2")