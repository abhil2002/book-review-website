# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import databases
import sqlalchemy
from databases import Database

DATABASE_URL = "sqlite:///./test.db"  # Use your preferred database URL here

metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, index=True),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("cover_image", sqlalchemy.String),
    sqlalchemy.Column("genre", sqlalchemy.String),
    sqlalchemy.Column("publication_date", sqlalchemy.String),
    sqlalchemy.Column("is_free_book", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    cover_image: str
    genre: str
    publication_date: str
    is_free_book: bool

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    query = books.insert().values(
        title=book.title,
        author=book.author,
        cover_image=book.cover_image,
        genre=book.genre,
        publication_date=book.publication_date,
        is_free_book=book.is_free_book,
    )
    last_record_id = await database.execute(query)
    return {**book.dict(), "id": last_record_id}



# ...

@app.get("/books/", response_model=list[Book])
async def read_books(skip: int = 0, limit: int = 10):
    query = books.select().offset(skip).limit(limit)
    result = await database.fetch_all(query)
    return result

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    query = books.select().where(books.c.id == book_id)
    book = await database.fetch_one(query)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    query = books.update().where(books.c.id == book_id).values(
        title=book.title,
        author=book.author,
        cover_image=book.cover_image,
        genre=book.genre,
        publication_date=book.publication_date,
        is_free_book=book.is_free_book,
    )
    await database.execute(query)
    updated_book = await read_book(book_id)
    return updated_book

@app.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int):
    query = books.delete().where(books.c.id == book_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}



from fastapi import HTTPException

# ...

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    query = books.update().where(books.c.id == book_id).values(
        title=book.title,
        author=book.author,
        cover_image=book.cover_image,
        genre=book.genre,
        publication_date=book.publication_date,
        is_free_book=book.is_free_book,
    )
    await database.execute(query)
    updated_book = await read_book(book_id)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}", response_model=dict)
async def delete_book(book_id: int):
    query = books.delete().where(books.c.id == book_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
