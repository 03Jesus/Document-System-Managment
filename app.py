import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from classes.document import Document
from logic.doc_controller import DocumentController

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
from typing import List
templates = Jinja2Templates(directory="templates")

app = FastAPI()
doc_object = DocumentController()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('./data/storage_doc.json', 'r', encoding='utf-8') as f:
    json_data = f.read()


parsed_json = json.loads(json_data)
output_json = json.dumps(parsed_json, ensure_ascii=False)
documents_array = parsed_json['documents']

resultados = []
for resultado in documents_array:
    if resultado['topic'] == 'fantasy':
        print(resultado['topic'])

@app.get("/")
def read_root():
    return {"200": "Welcome To Document Managment System Restful API"}


@app.get("/api/document")
async def root():
    return doc_object.show()

#Search by topic route
@app.get("/search", response_class=HTMLResponse)
async def search_documents(request: Request, theme: str = ''):
    results = []
    themes = get_all_themes()
    for document in documents_array:
        if not theme or theme == document['topic']:
            if theme.lower() in document['topic'].lower():
                results.append(document)
    return templates.TemplateResponse("search_results.html", {"request": request, "documents_array": results, "themes": themes})

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