from fastapi import FastAPI

from api import categories, books

app = FastAPI(title='Books API')

app.include_router(books.router)
app.include_router(categories.router)
