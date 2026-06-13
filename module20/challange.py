{
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": "1960",
    "genre": "Fiction / Southern Gothic"
},

{
    "title": "1984",
    "author": "George Orwell",
    "year": "1949",
    "genre": "Dystopian Fiction"
},

{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": "1937",
    "genre": "Fantasy"
}

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"title"}
