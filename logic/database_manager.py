import sqlite3


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('database\dmsdb.db')
        self.table_map = {
            'Book': 'books',
            'Ebook': 'ebooks',
            'AudioBook': 'audiobooks',
            # Agrega aquí los nombres de las clases de documentos adicionales y sus correspondientes nombres de tabla en la base de datos
        }

    def insert_document(self, document):
        try:
            table_name = self.table_map[type(document).__name__]
            cursor = self.conn.cursor()

            if table_name == 'books':
                cursor.execute("INSERT INTO books (book_author, book_title, book_price, book_topic, book_lang, book_publisher, book_editor, book_pages, book_synopsis, book_presentation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                    document.author, document.title, document.price, document.topic, document.language, document.publisher, document.editor, document.pages, document.synopsis, document.presentation))

            elif table_name == 'ebooks':
                cursor.execute('INSERT INTO ebooks (title, author, publisher, year_published, format, file_size) VALUES (?, ?, ?, ?, ?, ?)', (
                    document.title, document.author, document.publisher, document.year_published, document.format, document.file_size))
            elif table_name == 'audiobooks':
                cursor.execute('INSERT INTO audiobooks (title, author, narrator, length) VALUES (?, ?, ?, ?)', (
                    document.title, document.author, document.narrator, document.length))
            # Agrega aquí los bloques de código correspondientes para insertar en las tablas de documentos adicionales

            self.conn.commit()
        finally:
            cursor.close()
            self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect('database\dmsdb.db')

    def disconnect(self):
        self.conn.close()
