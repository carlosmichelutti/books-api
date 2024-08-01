from models.database import db_connection
from models.models import Books

from resources.schemas import (
    BookSchema,
    GetBooksSchema,
    CreateBooksSchema,
    UpdateBookSchema
)

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import select, func, delete, update
from flask_smorest import Blueprint, abort
from flask import make_response, jsonify
from flask.views import MethodView
import pandas as pd

blp = Blueprint("Books", __name__, description="Operations on books")

@blp.route(r'/books')
class BooksCategorysModelView(MethodView):

    @blp.arguments(schema=GetBooksSchema, location='query')
    @blp.response(status_code=200)
    def get(self: object, arguments: dict) -> dict:
        
        category = arguments.get('category')
        page_size = arguments.get('page_size')
        page = arguments.get('page')
        if category.lower() == 'all':
            result = select(
                Books
            ).limit(
                page_size
            ).offset(
                (page - 1) * page_size
            )
        
        else:
            result = select(
                Books
            ).where(
                func.lower(Books.category) == category.lower()
            ).limit(
                page_size
            ).offset(
                (page - 1) * page_size
            )
            
        dataframe = pd.read_sql(result, db_connection.engine)
        return dataframe.to_dict(orient='records')
    
    @blp.arguments(schema=CreateBooksSchema)
    @blp.response(status_code=201, schema=BookSchema(many=True))
    def post(self: object, books: dict) -> dict:

        created_books = []
        with db_connection.session as session:
            for book in books['books']:
                try:
                    session.add(Books(**book))
                    session.commit()
                    created_books.append(book)
                
                except IntegrityError:
                    abort(400, message=f'The book {book} already exists.')

                except SQLAlchemyError:
                    abort(500, message=f'An error occurred while creating the book {book}.')
        
        return make_response(jsonify({'message': 'Books created.', 'books': created_books}), 201)

@blp.route(r'/book/<int:book_id>')
class BookModelView(MethodView):
    
    @blp.response(status_code=200)
    def get(self: object, book_id: int) -> dict:

        try:
            book = select(
                Books
            ).where(
                Books.id == book_id
            )

            dataframe = pd.read_sql(book, db_connection.engine)
            return dataframe.to_dict(orient='records')

        except Exception as e:
            return abort(400, message='Book not found')

    @blp.arguments(schema=UpdateBookSchema, location='json')
    @blp.response(status_code=200, description="Book updated.")
    def put(self: object, book_data: dict, book_id: int):
        
        try:
            result = select(
                Books
            ).where(
                Books.id == book_id
            )

            dataframe = pd.read_sql(result, db_connection.engine)

            if not dataframe.empty:
                result = (
                    update(Books)
                    .where(Books.id == book_id)
                    .values(**book_data)
                )

                with db_connection.session as session:
                    session.execute(result)
                    session.commit()
            else:
                book = Books(id=book_id, **book_data)
                with db_connection.session as session:
                    session.add(book)
                    session.commit()

        except Exception as e:
            return abort(400, message='Book not found')

    @blp.response(status_code=200, description="Book deleted.")
    def delete(self: object, book_id: int) -> dict:
        
        try:
            result = (
                delete(Books)
                .where(Books.id == book_id)
            )

            with db_connection.session as session:
                session.execute(result)
                session.commit()
        
        except Exception as e:
            return abort(400, message='Book not found')