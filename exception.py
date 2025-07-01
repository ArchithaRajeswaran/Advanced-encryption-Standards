from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int

books_db = []

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.get("/books/")
def get_books():
    return books_db

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")

@app.post("/books/")
def add_book(book: Book):
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book already exists.")
    books_db.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            books_db[idx] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found.")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            deleted = books_db.pop(idx)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found.")

