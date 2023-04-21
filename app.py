import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from classes.document import Document
from logic.doc_controller import DocumentController
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

@app.get("/")
def read_root():
    return {"200": "Welcome To Document Managment System Restful API"}


@app.get("/api/document")
async def root():
    return doc_object.show()


@app.post("/api/document")
async def add(id: int, author: str, title: str, price: float, topic: str, language: str):
    return doc_object.add(Document(id=id, author=author, title=title, price=price, topic=topic, language=language))


if __name__ == "__main__":
    uvicorn.run(app, port=33507)