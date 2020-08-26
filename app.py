from controller.scraping import Masterdata, CustomTopik
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

api.add_resource(Masterdata, '/ambil')
api.add_resource(CustomTopik, '/ambil/<string:keyword>')


if __name__ == '__main__':
    app.run()