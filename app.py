from flask import Flask, jsonify, make_response, request
from pengineService import PengineService
import json

app = Flask(__name__)
pengineService = PengineService()

@app.route('/api/people/relative', methods = ['POST'])
def insertParentes():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertRelatives(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/professors', methods = ['POST'])
def insertProfessors():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertProfessors(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/students', methods = ['POST'])
def insertStudents():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertStudents(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/cases/confirmed', methods = ['POST'])
def insertConfirmedCases():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertConfirmedCases(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/cases/suspicious', methods = ['POST'])
def insertSuspiciousCases():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertSuspiciousCases(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/cases/death', methods = ['POST'])
def insertDeathCases():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.insertDeathCases(jsonData)
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

@app.route('/cases/non-infected/amount', methods = ['GET'])
def getNotInfected():
	queryResultDictionary = pengineService.getNonInfectedAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"nonInfectedPeopleAmount": quantity}

@app.route('/students/confirmed', methods = ['GET'])
def getConfirmedStudents():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosConfirmadosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"confirmedStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/confirmed/amount', methods = ['GET'])
def getConfirmedStudentsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosContaminadosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"confirmedStudentsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/city/confirmed', methods = ['GET'])
def getConfirmedStudentsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosContaminadosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"confirmedStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/students/vehicle/confirmed', methods = ['GET'])
def getConfirmedStudentsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosContaminadosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"confirmedStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)

@app.route('/students/suspect', methods = ['GET'])
def getSuspectStudents():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"suspectStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/suspect/amount', methods = ['GET'])
def getSuspectStudentsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosSuspeitosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"suspectStudentsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/city/suspect', methods = ['GET'])
def getSuspectStudentsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"suspectStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/students/vehicle/suspect', methods = ['GET'])
def getSuspectStudentsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"suspectStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)

@app.route('/students/dead', methods = ['GET'])
def getDeadStudents():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosMortosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"deadStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/dead/amount', methods = ['GET'])
def getDeadStudentsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosMortosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"deadStudentsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/students/city/dead', methods = ['GET'])
def getDeadStudentsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosMortosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"deadStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/students/vehicle/dead', methods = ['GET'])
def getDeadStudentsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosMortosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"deadStudents": alunos}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)

@app.route('/professors/confirmed', methods = ['GET'])
def getConfirmedProfessors():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"confirmedProfessores": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/confirmed/amount', methods = ['GET'])
def getConfirmedProfessorsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresContaminadosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"confirmedProfessorsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/city/confirmed', methods = ['GET'])
def getConfirmedProfessorsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"confirmedProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/professors/vehicle/confirmed', methods = ['GET'])
def getConfirmedProfessorsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"confirmedProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)
		
@app.route('/professors/suspect', methods = ['GET'])
def getSuspectProfessors():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"suspectProfessores": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/suspect/amount', methods = ['GET'])
def getSuspectProfessorsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresSuspeitosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"suspectProfessorsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/city/suspect', methods = ['GET'])
def getSuspectProfessorsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"suspectProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/professors/vehicle/suspect', methods = ['GET'])
def getSuspectProfessorsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"suspectProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)

@app.route('/professors/dead', methods = ['GET'])
def getDeadProfessors():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"deadProfessores": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/dead/amount', methods = ['GET'])
def getDeadProfessorsAmount():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresMortosPorTurmaESemestre(turma, semestre)
		quantity = 0
		for item in queryResultDictionary:
			quantity = item["Contador"]
		return {"deadProfessorsAmount": quantity}
	else:
		return make_response({"message": f"You might be missing parameters turma or semestre for this request."}, 400)

@app.route('/professors/city/dead', methods = ['GET'])
def getDeadProfessorsByCity():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"deadProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameters turma or cidade for this request."}, 400)
	
@app.route('/professors/vehicle/dead', methods = ['GET'])
def getDeadProfessorsByVehicle():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			professores.append(item["X"])
		return {"deadProfessors": professores}
	else:
		return make_response({"message": f"You might be missing parameter veiculo for this request."}, 400)


@app.route('/cases/confirmed/students/amount', methods = ['GET'])
def getAllStudentConfirmedCases():
	queryResultDictionary = pengineService.getAllStudentsConfirmedCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"confirmedStudentCasesAmount": quantity}

@app.route('/cases/suspicious/students/amount', methods = ['GET'])
def getAllStudentSuspiciousCases():
	queryResultDictionary = pengineService.getAllStudentsSuspiciousCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"suspiciousStudentCasesAmount": quantity}

@app.route('/cases/deaths/students/amount', methods = ['GET'])
def getAllStudentDeathCases():
	queryResultDictionary = pengineService.getAllStudentsDeathsAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"deadStudentCasesAmount": quantity}

@app.route('/cases/non-infected/students/amount', methods = ['GET'])
def getAllNonInfectedStudent():
	queryResultDictionary = pengineService.getAllUninfectedStudentsAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"nonInfectedStudentCasesAmount": quantity}

@app.route('/cases/confirmed/professors/amount', methods = ['GET'])
def getAllProfessorConfirmedCases():
	queryResultDictionary = pengineService.getAllProfessorsConfirmedCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"confirmedProfessorCasesAmount": quantity}

@app.route('/cases/suspicious/professors/amount', methods = ['GET'])
def getAllProfessorSuspiciousCases():
	queryResultDictionary = pengineService.getAllProfessorsSuspiciousCasesAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"suspiciousProfessorCasesAmount": quantity}

@app.route('/cases/deaths/professors/amount', methods = ['GET'])
def getAllProfessorDeathCases():
	queryResultDictionary = pengineService.getAllProfessorsDeathsAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"deadProfessorCasesAmount": quantity}

@app.route('/cases/non-infected/professors/amount', methods = ['GET'])
def getAllNonInfectedProfessor():
	queryResultDictionary = pengineService.getAllUninfectedProfessorsAmount()
	quantity = 0
	for item in queryResultDictionary:
		quantity = item["Counter"]
	return {"nonInfectedProfessorCasesAmount": quantity}

@app.route('/person/status/confirmed', methods = ['PUT'])
def updatePersonToConfirmed():
	data = request.get_json()
	nome = data.get('nome')
	if nome:
		pengineService.updatePersonStatusToConfirmed(nome)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)

@app.route('/person/status/suspect', methods = ['PUT'])
def updatePersonToSuspect():
	data = request.get_json()
	nome = data.get('nome')
	if nome:
		pengineService.updatePersonStatusToSuspect(nome)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)

@app.route('/person/status/dead', methods = ['PUT'])
def updatePersonToDead():
	data = request.get_json()
	nome = data.get('nome')
	if nome:
		pengineService.updatePersonStatusToDead(nome)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)

@app.route('/person/status/non-infected', methods = ['PUT'])
def updatePersonToNonInfected():
	data = request.get_json()
	nome = data.get('nome')
	if nome:
		pengineService.updatePersonStatusToNonInfected(nome)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)

@app.route('/students/confirmed/relatives', methods = ['GET'])
def getRelativesFromInfectedStudents():
	data = request.get_json()
	nome = data.get('nome')
	alunos = []
	if nome:
		queryResultDictionary = pengineService.buscaAlunosParentesDeUmAlunoInfectado(nome)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"parentesInfectados": alunos}
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)
	
@app.route('/professors/confirmed/relatives', methods = ['GET'])
def getRelativesFromInfectedProfessors():
	data = request.get_json()
	nome = data.get('nome')
	alunos = []
	if nome:
		queryResultDictionary = pengineService.buscaProfessoresParentesDeUmProfessorInfectado(nome)
		for item in queryResultDictionary:
			alunos.append(item["X"])
		return {"parentesInfectados": alunos}
	else:
		return make_response({"message": f"Está faltando o parâmetro nome."}, 400)
