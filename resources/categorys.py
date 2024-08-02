from models.database import db_connection
from models.models import Books

from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy import select
import pandas as pd

blp = Blueprint("Categorys", __name__, description="Operations on books categorys")

@blp.route(r'/categorys')
class BooksCategorysModelView(MethodView):

    def get(self: object) -> dict:

        query = select(
            Books.category
        ).distinct()

        dataframe = pd.read_sql(query, db_connection.engine)
        
        return {'categorys': dataframe['category'].to_list()}