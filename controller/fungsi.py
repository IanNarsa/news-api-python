from flask_restful import Resource
from flask import Flask, jsonify, request
from controller.scraping import getContent

import sys
sys.path.append("..")
from configapi.dbconfig import configdb
import requests
class Masterdata(Resource):
  def get(self):
    URL = "http://newsapi.org/v2/top-headlines?country=id&apiKey=xxxx"
    r = requests.get(url = URL) 
    return r.json()