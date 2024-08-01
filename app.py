from resources.categorys import blp as CategorysBlueprint
from resources.books import blp as BooksBlueprint

from flask_smorest import Api
from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Books REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(BooksBlueprint)
api.register_blueprint(CategorysBlueprint)

app.run(port=5000, host='localhost', debug=True)