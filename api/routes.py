from flask import jsonify, request
from .config import API_KEY
from .models import new_list


def get_news():

    news_data = [{"tit": news.tit, "des": news.des, "img": news.img} for news in new_list]

    api_key = request.args.get("api_key")

    if api_key is None and len(request.args) > 0:
        return jsonify({"Error": "Invalid query parameters"})

    if api_key and api_key != API_KEY:
        return jsonify({"Error": "Invalid api key"})

    return jsonify({"news": news_data})