from typing import Union
from classes.audiobook import AudioBook
from classes.ebook import Ebook
from classes.book import Book
from classes.document import Document
from logic.database_manager import DatabaseManager
import json
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class DocumentController(object):

    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage_doc.json')
        self.db_manager = DatabaseManager()

    def add(self, document: Document = Union[Book, Ebook, AudioBook]) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['documents'].append(document.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        self.db_manager.insert_document(document)
        return document.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
