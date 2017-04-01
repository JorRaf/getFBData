
import urllib2
import json
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.test_database
from datetime import datetime


dados_json  =   open('config.json','r')
config =   json.load(dados_json)

api_version = config['api_version']
page_target = config['page_target']
data_type   = config['data_type']
token       = config['token']
graph_url = config['graph_url'] + api_version +"/" + page_target +"/" + data_type + "?access_token=" + token

result = db.FBComments.insert_one(json.loads(urllib2.urlopen(graph_url).read()))
