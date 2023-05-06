import sqlite3
import os
PATH = os.getcwd()
DIR_DATA = PATH + '{0}database{0}'.format(os.sep)
file = '{0}{1}'.format(DIR_DATA, 'utb.sqlite3')
print(file)


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(file)
        self.table_map = {
            'Book': 'books',
            'Ebook': 'ebooks',
            'AudioBook': 'audiobooks',
            'Magazine': 'magazines',
            'InvBook': 'inv_books',
        }

    def insert_document(self, document):
        try:
            table_name = self.table_map[type(document).__name__]
            conn = sqlite3.connect(file)
            cursor = conn.cursor()

            if table_name == 'audiobooks':
                cursor.execute('INSERT INTO audiobooks (author, title, price, topic, language, pub_date, size, doi, duration, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.duration, document.synopsis))

            elif table_name == 'books':
                cursor.execute("INSERT INTO books (author, title, price, topic, language, pub_date, publisher, editor, pages, synopsis, presentation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.publisher, document.editor, document.pages, document.synopsis, document.presentation))               

            elif table_name == 'ebooks':
                cursor.execute('INSERT INTO ebooks (author, title, price, topic, language, pub_date, size, doi, editor, pages, synopsis) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.editor, document.pages, document.synopsis))               
                
            elif table_name == 'inv_books':
                cursor.execute('INSERT INTO inv_books (author, title, price, topic, language, pub_date, size, doi, pages, abstract) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.pages, document.abstract))               
            
            elif table_name == 'magazines':
                cursor.execute('INSERT INTO magazines (author, title, price, topic, language, pub_date, size, doi, edition, pages) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                    document.author, document.title, document.price, document.topic, document.language, document.pub_date, document.size, document.doi, document.edition, document.pages))               
        finally:
            conn.commit()
            conn.close()

    def get_documents(self, document_type: str):
        try:
            conn = sqlite3.connect(file)
            cursor = conn.cursor()
            #If the user dosent select a document type, it will return all documents
            #else it will return the documents of the type selected
            if document_type == '':
                cursor.execute('SELECT * FROM books')
                rows = cursor.fetchall()
                cursor.execute('SELECT * FROM ebooks')
                rows += cursor.fetchall()
                cursor.execute('SELECT * FROM audiobooks')
                rows += cursor.fetchall()
                cursor.execute('SELECT * FROM magazines')
                rows += cursor.fetchall()
                cursor.execute('SELECT * FROM inv_books')
                rows += cursor.fetchall()
                print("Printed all documents")
                return rows                
            else:
                cursor.execute('SELECT * FROM {}'.format(document_type))
                rows = cursor.fetchall()
                print("Printed all {} documents".format(document_type))
                return rows
        finally:
            print("Printed")
    def connect(self):
        self.conn = sqlite3.connect(file)

    def disconnect(self):
        self.conn.close()
