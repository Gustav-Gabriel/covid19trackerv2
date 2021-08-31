from flask import Flask, jsonify, make_response, request
from pengineService import PengineService
import json

app = Flask(__name__)
pengineService = PengineService()

@app.route('/api/pessoas/parentes', methods = ['POST'])
def inserirParentes():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirParentes(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/professores', methods = ['POST'])
def inserirProfessors():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirProfessores(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/alunos', methods = ['POST'])
def inserirAlunos():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirAlunos(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/casos/confirmados', methods = ['POST'])
def inserirCasosConfirmados():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirCasosConfirmados(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/casos/suspeitas', methods = ['POST'])
def inserirCasosSuspeitas():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirCasosDeSuspeita(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/casos/mortos', methods = ['POST'])
def inserirCasosMorte():
	data = request.get_json()
	jsonData = json.dumps(data)
	pengineService.inserirCasosDeMorte(jsonData)
	return f"Os dados foram cadastrados com sucesso!."

@app.route('/api/casos/confirmados/quantidade', methods = ['GET'])
def buscarQuantidadeDeCasosConfirmados():
	queryResultDictionary = pengineService.buscarQuantidadeDeCasosConfirmados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeDeCasosConfirmados": quantidade}

@app.route('/api/casos/suspeitas/quantidade', methods = ['GET'])
def buscarQuantidadeDeCasosComSuspeita():
	queryResultDictionary = pengineService.buscarQuantidadeDeCasosDeSuspeita()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeDeCasosComSuspeita": quantidade}

@app.route('/api/casos/mortes/quantidade', methods = ['GET'])
def buscarQuantidadeDeMortes():
	queryResultDictionary = pengineService.buscarQuantidadeDeMortos()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeDeMortes": quantidade}

@app.route('/api/casos/nao-infectados/quantidade', methods = ['GET'])
def buscarQuantidadeDeCasosNaoInfectados():
	queryResultDictionary = pengineService.buscarQuantidadeDeNaoInfectados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeDeCasosDeNaoInfeccao": quantidade}

@app.route('/api/alunos/confirmados', methods = ['GET'])
def buscaAlunosConfirmados():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosConfirmadosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosConfirmados": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/confirmados/quantidade', methods = ['GET'])
def buscaQuantidadeDeAlunosConfirmados():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosContaminadosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeAlunosConfirmados": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/cidade/confirmados', methods = ['GET'])
def buscaAlunosConfirmadosPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosContaminadosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosConfirmados": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/alunos/veiculo/confirmados', methods = ['GET'])
def buscaAlunosConfirmadosPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosContaminadosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosConfirmados": alunos}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro veículo."}, 400)

@app.route('/api/alunos/suspeitas', methods = ['GET'])
def buscaAlunosComSuspeita():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosComSuspeita": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/suspeitas/quantidade', methods = ['GET'])
def buscaQuantidadeDeAlunosComSuspeita():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosSuspeitosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeAlunosComSuspeita": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/cidade/suspeitas', methods = ['GET'])
def buscaAlunosComSuspeitaPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosComSuspeita": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/alunos/veiculo/suspeitas', methods = ['GET'])
def buscaAlunosComSuspeitaPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosSuspeitosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosComSuspeita": alunos}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro veículo."}, 400)

@app.route('/api/alunos/mortos', methods = ['GET'])
def buscaAlunosMortos():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	alunos = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaAlunosMortosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosMortos": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/morte/quantidade', methods = ['GET'])
def buscaQuantidadeDeAlunosMortos():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeAlunosMortosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeAlunosMortos": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/alunos/cidade/mortos', methods = ['GET'])
def buscaAlunosMortosPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	alunos = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaAlunosMortosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosMortos": alunos}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/alunos/veiculo/mortos', methods = ['GET'])
def buscaAlunosMortosPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	alunos = []
	if veiculo:
		queryResultDictionary = pengineService.buscaAlunosMortosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"alunosMortos": alunos}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro veículo."}, 400)

@app.route('/api/professores/confirmados', methods = ['GET'])
def buscaProfessoresConfirmados():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresConfirmados": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/confirmados/quantidade', methods = ['GET'])
def buscaQuantidadeDeProfessoresConfirmados():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresContaminadosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeProfessoresConfirmados": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/cidade/confirmados', methods = ['GET'])
def buscaProfessoresConfirmadosPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresConfirmados": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/professores/veiculo/confirmados', methods = ['GET'])
def buscaProfessoresConfirmadosPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresContaminadosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresConfirmados": professores}
	else:
		return make_response({"mensage": f"Está faltando o parâmetro veículo."}, 400)
		
@app.route('/api/professores/suspeitas', methods = ['GET'])
def buscaProfessoresComSuspeita():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresComSuspeita": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/suspeitas/quantidade', methods = ['GET'])
def buscaQuantidadeDeProfessoresComSuspeita():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresSuspeitosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeProfessoresComSuspeita": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/cidade/suspeitas', methods = ['GET'])
def buscaProfessoresComSuspeitaPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresComSuspeita": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/professores/veiculo/suspeitas', methods = ['GET'])
def buscaProfessoresComSuspeitaPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresSuspeitosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresComSuspeita": professores}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro veículo."}, 400)

@app.route('/api/professores/mortos', methods = ['GET'])
def buscaProfessoresMortos():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	professores = []
	if turma and semestre:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorTurmaESemestre(turma, semestre)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresMortos": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/mortos/quantidade', methods = ['GET'])
def buscaQuantidadeDeProfessoresMortos():
	data = request.get_json()
	turma = data.get('turma')
	semestre = data.get('semestre')
	if turma and semestre:
		queryResultDictionary = pengineService.buscaQuantidadeDeProfessoresMortosPorTurmaESemestre(turma, semestre)
		quantidade = 0
		for item in queryResultDictionary:
			quantidade = item["C"]
		return {"quantidadeDeProfessoresMortos": quantidade}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou semestre."}, 400)

@app.route('/api/professores/cidade/mortos', methods = ['GET'])
def buscaProfessoresMortosPorCidade():
	data = request.get_json()
	turma = data.get('turma')
	cidade = data.get('cidade')
	professores = []
	if turma and cidade:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorTurmaECidade(turma, cidade)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresMortos": professores}
	else:
		return make_response({"mensagem": f"Podem estar faltando os parâmetros turma e/ou cidade."}, 400)
	
@app.route('/api/professores/veiculo/mortos', methods = ['GET'])
def bsucaProfessoresMortosPorVeiculo():
	data = request.get_json()
	veiculo = data.get('veiculo')
	professores = []
	if veiculo:
		queryResultDictionary = pengineService.buscaProfessoresMortosPorVeiculo(veiculo)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"professoresMortos": professores}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro veículo."}, 400)


@app.route('/api/casos/confirmados/alunos/quantidade', methods = ['GET'])
def buscaQuantidadaTotalDeAlunosConfirmados():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeAlunosConfirmados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeAlunosConfirmados": quantidade}

@app.route('/api/casos/suspeitas/alunos/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeAlunosComSuspeita():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeAlunosComSuspeita()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeAlunosComSuspeita": quantidade}

@app.route('/api/casos/mortos/alunos/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeAlunosMortos():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeAlunosMortos()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeAlunosMortos": quantidade}

@app.route('/api/casos/nao-infectados/alunos/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeAlunosNaoInfectados():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeAlunosNaoInfectados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeAlunosNaoInfectados": quantidade}

@app.route('/api/casos/confirmados/professores/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeProfessoresConfirmados():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeProfessoresConfirmados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quanditadeTotalDeProfessoresConfirmados": quantidade}

@app.route('/api/casos/suspeitas/professores/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeProfessoresComSuspeita():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeProfessoresComSuspeita()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeProfessoresComSuspeita": quantidade}

@app.route('/api/casos/mortos/professores/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeProfessoreMortos():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeProfessoresMortos()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"buscaQuantidadeTotalDeProfessoresMortos": quantidade}

@app.route('/api/casos/nao-infectados/professores/quantidade', methods = ['GET'])
def buscaQuantidadeTotalDeProfessoresNaoInfectados():
	queryResultDictionary = pengineService.buscarQuantidadeTotalDeProfessoresNaoInfectados()
	quantidade = 0
	for item in queryResultDictionary:
		quantidade = item["C"]
	return {"quantidadeTotalDeProfessoresNaoInfectados": quantidade}

@app.route('/api/pessoa/status/confirmados', methods = ['PUT'])
def atualizaStatusDaPessoaParaConfirmado():
	data = request.get_json()
	registro = data.get('registro')
	if registro:
		pengineService.atualizarStatusDaPessoaParaConfirmada(registro)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/pessoa/status/suspeita', methods = ['PUT'])
def atualizaStatusdaPessoaParaSuspeita():
	data = request.get_json()
	registro = data.get('registro')
	if registro:
		pengineService.atualizarStatusDaPessoaParaSuspeita(registro)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/pessoa/status/morta', methods = ['PUT'])
def atualizaStatusDaPessoaParaMorta():
	data = request.get_json()
	registro = data.get('registro')
	if registro:
		pengineService.atualizarStatusDaPessoaParaMorta(registro)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/pessoa/status/nao-infectada', methods = ['PUT'])
def atualizaStatusDaPessoaParaNaoInfectada():
	data = request.get_json()
	registro = data.get('registro')
	if registro:
		pengineService.atualizaStatusDaPessoaParaNaoInfectada(registro)
		return f"Status atualizado com sucesso!."
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/alunos/confirmados/parentes', methods = ['GET'])
def buscaAlunosParentesDeUmAlunoInfectado():
	data = request.get_json()
	registro = data.get('registro')
	alunos = []
	if registro:
		queryResultDictionary = pengineService.buscaAlunosParentesDeUmAlunoInfectado(registro)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			alunos.append(json.loads(objetoString))
		return {"parentesInfectados": alunos}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)
	
@app.route('/api/professores/confirmados/parentes', methods = ['GET'])
def buscaProfessoreParentesDeUmProfessorInfectado():
	data = request.get_json()
	registro = data.get('registro')
	professores = []
	if registro:
		queryResultDictionary = pengineService.buscaProfessoresParentesDeUmProfessorInfectado(registro)
		for item in queryResultDictionary:
			objetoString = json.dumps({"registro": item["X"], "nome": item["N"]})
			professores.append(json.loads(objetoString))
		return {"parentesInfectados": professores}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/professores/professor/confirmado/turmas', methods = ['GET'])
def buscaTurmasDeUmProfessorConfirmado():
	data = request.get_json()
	registro = data.get('registro')
	professores = []
	if registro:
		queryResultDictionary = pengineService.buscaTurmasDeUmProfessorConfirmado(registro)
		for item in queryResultDictionary:
			objetoString = json.dumps({"turma": item["T"]})
			professores.append(json.loads(objetoString))
		return {"turmas": professores}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)

@app.route('/api/professores/professor/suspeita/turmas', methods = ['GET'])
def buscaTurmasDeUmProfessorComSuspeita():
	data = request.get_json()
	registro = data.get('registro')
	professores = []
	if registro:
		queryResultDictionary = pengineService.buscaTurmasDeUmProfessorComSuspeita(registro)
		for item in queryResultDictionary:
			objetoString = json.dumps({"turma": item["T"]})
			professores.append(json.loads(objetoString))
		return {"turmas": professores}
	else:
		return make_response({"mensagem": f"Está faltando o parâmetro registro."}, 400)
