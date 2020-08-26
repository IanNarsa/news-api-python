from flask_restful import Resource
from flask import Flask, jsonify, request
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='xxxxxx')
class Masterdata(Resource):
    def get(self):
        top_headlines = newsapi.get_top_headlines(country='id')
        return top_headlines

class CustomTopik(Resource):
    def get(self,keyword):
        top_headlines = newsapi.get_top_headlines(
            country='id',
            category=keyword)
        return top_headlines