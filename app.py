import uvicorn
from fastapi import FastAPI, Request, Form
from starlette.middleware.cors import CORSMiddleware
import sqlite3

from classes.document import Document
from classes.book import Book
from classes.ebook import Ebook
from classes.audiobook import AudioBook
from classes.invbook import InvBook
from classes.magazine import Magazine
from logic.doc_controller import DocumentController
from logic.database_manager import DatabaseManager

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
from typing import List
from datetime import date

templates = Jinja2Templates(directory="templates")

app = FastAPI()
doc_object = DatabaseManager()
origins = [
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('./data/langs.json', 'r', encoding='utf-8') as f:
    languages = json.load(f)

with open('./data/storage_doc.json', 'r', encoding='utf-8') as f:
    json_data = f.read()


parsed_json = json.loads(json_data)
output_json = json.dumps(parsed_json, ensure_ascii=False)


@app.get("/")
def read_root():
    return {"200": "Welcome To Document Managment System Restful API"}


@app.get("/api/document")
async def root():
    return doc_object.show()


@app.get("/search", response_class=HTMLResponse)
async def search_documents(request: Request, theme: str = ''):
    themes = ["books", "ebooks", "audiobooks", "magazines", "inv_books"]
    print(theme)
    results = doc_object.get_documents(theme)
    print(results)
    return templates.TemplateResponse("search_results.html", {"request": request, "documents_array": results, "themes": themes})


@app.get("/add-document-form", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("add_documents.html", {"request": request, "languages": languages})


@app.post("/process-document-form", response_class=HTMLResponse)
async def add_document(request: Request, document_type: str = Form(...),
                       author: str = Form(...), title: str = Form(...),
                       price: float = Form(...), topic: str = Form(...), language: str = Form(...),
                       pub_date: date = Form(None), size: float = Form(None), doi: str = Form(None),
                       publisher: str = Form(None), editor: str = Form(None), pages: int = Form(None),
                       synopsis: str = Form(None), presentation: str = Form(None), edition: int = Form(None),
                       duration: int = Form(None), abstract: str = Form(None)):
    if document_type == "audiobook":
        try:
            audiobook_form = AudioBook(author=author, title=title, price=price, topic=topic, language=language,
                                       pub_date=pub_date, size=size, doi=doi, duration=duration, synopsis=synopsis)
            doc_object.insert_document(audiobook_form)
            return templates.TemplateResponse("success.html", {"request": request, "document_type": document_type.capitalize()})
        except ValueError as e:
            # Retur alert error
            message = "Error al procesar el formulario, por favor inténtelo de nuevo: " + \
                str(e)
            return f"""
            <script>
                alert(`{message}`);
                window.location.replace("./formulario");
            </script>
            """

    elif document_type == "book":
        try:
            book_form = Book(author=author, title=title, price=price, topic=topic, language=language,
                             publisher=publisher, editor=editor, pages=pages, synopsis=synopsis, presentation=presentation)
            doc_object.insert_document(book_form)
            return templates.TemplateResponse("success.html", {"request": request, "document_type": document_type.capitalize()})
        except ValueError as e:
            # Retur alert error
            message = "Error al procesar el formulario, por favor inténtelo de nuevo: " + \
                str(e)
            return f"""
            <script>
                alert(`{message}`);
                window.location.replace("./formulario");
            </script>
            """
    elif document_type == "ebook":
        try:
            ebook_form = Ebook(author=author, title=title, price=price, topic=topic, language=language,
                               pub_date=pub_date.isoformat(), size=size, doi=doi, editor=editor, pages=pages, synopsis=synopsis)
            doc_object.insert_document(ebook_form)
            return templates.TemplateResponse("success.html", {"request": request, "document_type": document_type})
        except ValueError as e:
            # Retur alert error
            message = "Error al procesar el formulario, por favor inténtelo de nuevo: " + \
                str(e)
            return f"""
            <script>
                alert(`{message}`);
                window.location.replace("./formulario");
            </script>
            """
        
    elif document_type == "invbook":
        try:
            invbook_form = InvBook(author=author, title=title, price=price, topic=topic, language=language,
                                   pub_date=pub_date.isoformat(), size=size, doi=doi, pages=pages, abstract=abstract)
            doc_object.insert_document(invbook_form)
            return templates.TemplateResponse("success.html", {"request": request, "document_type": document_type})
        except ValueError as e:
            # Retur alert error
            message = "Error al procesar el formulario, por favor inténtelo de nuevo: " + \
                str(e)
            return f"""
            <script>
                alert(`{message}`);
                window.location.replace("./formulario");
            </script>
            """
    elif document_type == "magazine":
        try:
            magazine_form = Magazine(author=author, title=title, price=price, topic=topic, language=language,
                                     pub_date=pub_date.isoformat(), size=size, doi=doi, edition=edition, pages=pages)
            doc_object.insert_document(magazine_form)
            return templates.TemplateResponse("success.html", {"request": request, "document_type": document_type})
        except ValueError as e:
            # Retur alert error
            message = "Error al procesar el formulario, por favor inténtelo de nuevo: " + \
                str(e)
            return f"""
            <script>
                alert(`{message}`);
                window.location.replace("./formulario");
            </script>
            """

def get_all_themes() -> List[str]:
    themes = set()
    for document in documents_array:
        themes.add(document['topic'])
    return sorted(list(themes))


@app.post("/api/document")
async def add(id: int, author: str, title: str, price: float, topic: str, language: str):
    return doc_object.add(Document(id=id, author=author, title=title, price=price, topic=topic, language=language))


if __name__ == "__main__":
    uvicorn.run(app, port=33507)
