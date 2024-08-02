from models.database import db_connection
from models.models import Books

from marshmallow.validate import OneOf
from marshmallow import Schema, fields
from sqlalchemy import select
import pandas as pd

class BookSchema(Schema):
    category = fields.Str(required=True)
    title = fields.Str(required=True)
    price = fields.Str(required=True)

class GetBooksSchema(Schema):
    category = fields.Str(required=True, validate=OneOf(['All'] + pd.read_sql(select(Books.category).distinct(), db_connection.engine)['category'].to_list()))
    page = fields.Int(default=1)
    page_size = fields.Int(default=10)

class CreateBooksSchema(Schema):
    books = fields.List(fields.Nested(BookSchema), required=True)
                         
class GetBookSchema(Schema):
    book_id = fields.Int(required=True)

class DeleteBookSchema(Schema):
    id = fields.Int(required=True)

class UpdateBookSchema(Schema):
    category = fields.Str()
    title = fields.Str()
    price = fields.Str()