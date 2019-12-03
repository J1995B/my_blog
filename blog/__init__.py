from flask import Blueprint
from flask_restplus import Api

from blog.article import ArticleApi

article_api = Blueprint('article_api', __name__)
art_api = Api(article_api, version='v1', doc=False)
art_api.add_namespace(ArticleApi, '')
