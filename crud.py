from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic schema
class Book(BaseModel):
    id: int
    title: str
    author: str
    pages: int

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}


# In-memory "database"
books_db = []

# GET all books
@app.get("/books/")
def get_books():
    return books_db


# POST add a new book
@app.post("/books/")
def add_book(book: Book):
    # Check if book with same id exists
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book already exists.")
    books_db.append(book)
    return book

# PUT update a book
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
