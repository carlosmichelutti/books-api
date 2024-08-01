from sqlalchemy import select, func, delete, update
from models.database import db_connection
from flask_smorest import Blueprint, abort
from flask import request, make_response
from models.models import Books
from flask.views import MethodView
import pandas as pd

blp = Blueprint("Categorys", __name__, description="Operations on books categorys")

@blp.route(r'/categorys', methods=['GET'])
class BooksCategorysModelView(MethodView):

    def get(self: object) -> dict:

        query = select(
            Books.category
        ).distinct()

        dataframe = pd.read_sql(query, db_connection.engine)
        
        return {'categorys': dataframe['category'].to_list()}