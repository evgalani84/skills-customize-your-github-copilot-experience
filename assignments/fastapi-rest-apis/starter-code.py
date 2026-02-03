from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int


# In-memory data store
books: List[Book] = [
    Book(id=1, title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", pages=224),
    Book(id=2, title="1984", author="George Orwell", pages=328),
]


@app.get("/books", response_model=List[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for b in books:
        if b.id == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book with this id already exists")
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated: Book):
    for i, b in enumerate(books):
        if b.id == book_id:
            books[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b.id == book_id:
            books.pop(i)
            return
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
