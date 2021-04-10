from flask import Flask, jsonify, make_response, request
from pengineService import PengineService
import json

app = Flask(__name__)
pengineService = PengineService()

@app.route('/database/insert/json', methods = ['POST'])
def addToDatabase():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertDatabaseThroughJson(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/cases/confirmed/amount', methods = ['GET'])
def getConfirmedCases():
	queryResultDictionary = pengineService.getConfirmedCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"confirmedCasesAmount": quantity}

@app.route('/cases/suspicious/amount', methods = ['GET'])
def getSuspiciousCases():
	queryResultDictionary = pengineService.getSuspiciousCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"suspiciousCasesAmount": quantity}

@app.route('/cases/deaths/amount', methods = ['GET'])
def getDeaths():
	queryResultDictionary = pengineService.getDeathsAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"deathsAmount": quantity}
