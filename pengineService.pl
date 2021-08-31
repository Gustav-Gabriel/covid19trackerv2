% inicio da aplicacao em prolog configurando pengine e funcoes
:- module(pengineService,
    [ inserir_parentes/1
    , inserir_professores/1
    , inserir_alunos/1
    , inserir_casos_confirmados/1
    , inserir_casos_suspeitos/1
    , inserir_casos_morte/1
    , busca_quantidade_casos_confirmados/2
    , busca_quantidade_casos_suspeitos/2
    , busca_quantidade_casos_morte/2
    , busca_quantidade_de_pessoas_nao_contaminadas/2
    , busca_alunos_contaminados_por_turma_e_semestre/3
    , busca_quantidade_de_alunos_contaminados_por_turma_e_semestre/4
    , busca_alunos_contaminados_por_turma_e_cidade/3
    , busca_alunos_contaminados_por_veiculo/2
    , busca_alunos_suspeitos_por_turma_e_semestre/3
    , busca_quantidade_de_alunos_suspeitos_por_turma_e_semestre/4
    , busca_alunos_suspeitos_por_turma_e_cidade/3
    , busca_alunos_suspeitos_por_veiculo/2
    , busca_alunos_mortos_por_turma_e_semestre/3
    , busca_quantidade_de_alunos_mortos_por_turma_e_semestre/4
    , busca_alunos_mortos_por_turma_e_cidade/3
    , busca_alunos_mortos_por_veiculo/2
    , busca_professores_contaminados_por_turma_e_semestre/3
    , busca_quantidade_de_professores_contaminados_por_turma_e_semestre/4
    , busca_professores_contaminados_por_turma_e_cidade/3
    , busca_professores_contaminados_por_veiculo/2
    , busca_professores_suspeitos_por_turma_e_semestre/3
    , busca_quantidade_de_professores_suspeitos_por_turma_e_semestre/4
    , busca_professores_suspeitos_por_turma_e_cidade/3
    , busca_professores_suspeitos_por_veiculo/2
    , busca_professores_mortos_por_turma_e_semestre/3
    , busca_quantidade_de_professores_mortos_por_turma_e_semestre/4
    , busca_professores_mortos_por_turma_e_cidade/3
    , busca_professores_mortos_por_veiculo/2
    , busca_quantidade_alunos_confirmados/2
    , busca_quantidade_alunos_suspeitos/2
    , busca_quantidade_alunos_mortos/2
    , busca_quantidade_de_alunos_nao_contaminadas/2
    , busca_quantidade_professores_confirmados/2
    , busca_quantidade_professores_suspeitos/2
    , busca_quantidade_professores_mortos/2
    , busca_quantidade_de_professores_nao_contaminadas/2
    , atualizar_pessoa_para_confirmada/1
    , atualizar_pessoa_para_suspeita/1
    , atualizar_pessoa_para_morta/1
    , atualizar_pessoa_para_nao_infectada/1
    , busca_alunos_parentes_de_outro_aluno_infectado/2
    , busca_professores_parentes_de_outro_professor_infectado/2
    ]
).

% uso de bibliotecas
:- use_module(library(persistency)).
:- use_module(library(http/json)).

% regra principal para inserir qualquer predicato 
:- persistent fact(fact1:any).

% Arquivo onde linhas salvas representam o banco de dados
:- db_attach('database_v3.pl', []).

% Funcao recursiva para inserir varios predicatos
adicionar_todos_predicatos([]).
adicionar_todos_predicatos([Atual|Resto]) :- assert_fact(Atual), nl, print(Atual), nl, adicionar_todos_predicatos(Resto).

% inserts by predicate

inserir_parentes(Json) :-
	atom_json_dict(Json, DicionarioDeParentes1, [default_tag(parente)]),
    dicts_to_compounds(DicionarioDeParentes1.parentes, [parente1, parente2], dict_fill(null), Parentes1),
    adicionar_todos_predicatos(Parentes1),
    atom_json_dict(Json, DicionarioDeParentes2, [default_tag(parente)]),
    dicts_to_compounds(DicionarioDeParentes2.parentes, [parente2, parente1], dict_fill(null), Parentes2),
    adicionar_todos_predicatos(Parentes2).

inserir_professores(Json) :-
	atom_json_dict(Json, DicionarioDeProfessoresPessoa, [default_tag(pessoa)]),
    dicts_to_compounds(DicionarioDeProfessoresPessoa.professores, [nome], dict_fill(null), Pessoas),
    adicionar_todos_predicatos(Pessoas),

	atom_json_dict(Json, DicionarioDeProfessores, [default_tag(professor)]),
    dicts_to_compounds(DicionarioDeProfessores.professores, [nome], dict_fill(null), Professores),
    adicionar_todos_predicatos(Professores),

    atom_json_dict(Json, DicionarioDeProfessoresPorTurma, [default_tag(professor_turma)]),
    dicts_to_compounds(DicionarioDeProfessoresPorTurma.professoresTurma, [nome, turma], dict_fill(null), ProfessoresTurma),
    adicionar_todos_predicatos(ProfessoresTurma),

    atom_json_dict(Json, DicionarioDeProfessoresPorSemestre, [default_tag(professor_semestre)]),
    dicts_to_compounds(DicionarioDeProfessoresPorSemestre.professoresSemestre, [nome, semestre], dict_fill(null), ProfessoresSemestre),
    adicionar_todos_predicatos(ProfessoresSemestre),

    atom_json_dict(Json, DicionarioDeProfessoresPorTransporte, [default_tag(professor_transporte)]),
    dicts_to_compounds(DicionarioDeProfessoresPorTransporte.professoresTransporte, [nome, transporte], dict_fill(null), ProfessoresTransporte),
    adicionar_todos_predicatos(ProfessoresTransporte),

    atom_json_dict(Json, DicionarioDeProfessoresPorCidade, [default_tag(professor_cidade)]),
    dicts_to_compounds(DicionarioDeProfessoresPorCidade.professoresCidade, [nome, cidade], dict_fill(null), ProfessoresCidade),
    adicionar_todos_predicatos(ProfessoresCidade).

inserir_alunos(Json) :-
	atom_json_dict(Json, DicionarioDeAlunosPessoa, [default_tag(pessoa)]),
    dicts_to_compounds(DicionarioDeAlunosPessoa.alunos, [nome], dict_fill(null), Pessoas),
    adicionar_todos_predicatos(Pessoas),
    atom_json_dict(Json, DicionarioDeAlunos, [default_tag(aluno)]),
    dicts_to_compounds(DicionarioDeAlunos.alunos, [nome], dict_fill(null), Alunos),
    adicionar_todos_predicatos(Alunos),
    atom_json_dict(Json, DicionarioDeAlunosPorTurma, [default_tag(aluno_turma)]),
    dicts_to_compounds(DicionarioDeAlunosPorTurma.alunosTurma, [nome, turma], dict_fill(null), AlunosTurma),
    adicionar_todos_predicatos(AlunosTurma),
    atom_json_dict(Json, DicionarioDeAlunosPorSemestre, [default_tag(aluno_semestre)]),
    dicts_to_compounds(DicionarioDeAlunosPorSemestre.alunosSemestre, [nome, semestre], dict_fill(null), AlunosSemestre),
    adicionar_todos_predicatos(AlunosSemestre),
    atom_json_dict(Json, DicionarioDeAlunosPorTransporte, [default_tag(aluno_transporte)]),
    dicts_to_compounds(DicionarioDeAlunosPorTransporte.alunosTransporte, [nome, transporte], dict_fill(null), AlunosTransporte),
    adicionar_todos_predicatos(AlunosTransporte),
    atom_json_dict(Json, DicionarioDeAlunosPorCidade, [default_tag(aluno_cidade)]),
    dicts_to_compounds(DicionarioDeAlunosPorCidade.alunosCidade, [nome, cidade], dict_fill(null), AlunosCidade),
    adicionar_todos_predicatos(AlunosCidade).

inserir_casos_confirmados(Json) :-
	atom_json_dict(Json, DicionarioCasosConfirmados, [default_tag(confirmado)]),
    dicts_to_compounds(DicionarioCasosConfirmados.confirmados, [nome], dict_fill(null), Confirmados),
    adicionar_todos_predicatos(Confirmados).

inserir_casos_suspeitos(Json) :-
    atom_json_dict(Json, DicionarioCasosSuspeitos, [default_tag(suspeito)]),
    dicts_to_compounds(DicionarioCasosSuspeitos.suspeitos, [nome], dict_fill(null), Suspeitos),
    adicionar_todos_predicatos(Suspeitos).

inserir_casos_morte(Json) :-
    atom_json_dict(Json, DicionarioCasosMorte, [default_tag(morte)]),
    dicts_to_compounds(DicionarioCasosMorte.mortes, [nome], dict_fill(null), Mortes),
    adicionar_todos_predicatos(Mortes).


% regras para recuperar quantidades por status
busca_quantidade_casos_confirmados(X, Confirmados) :-
    aggregate_all(count, fact(confirmado(X)), Confirmados).

busca_quantidade_casos_suspeitos(X, Suspeitas) :-
    aggregate_all(count, fact(suspeito(X)), Suspeitas).

busca_quantidade_casos_morte(X, Mortes) :-
    aggregate_all(count, fact(morte(X)), Mortes).

busca_quantidade_de_pessoas_nao_contaminadas(Pessoa, NaoContaminados) :-
    aggregate_all(count, (\+fact(confirmado(Pessoa)), \+fact(suspeito(Pessoa)), \+fact(morte(Pessoa))), NaoContaminados).

%Alunos contaminados
busca_alunos_contaminados_por_turma_e_semestre(Aluno, Turma, Semestre) :- 
	fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(confirmado(Aluno)).
	
busca_quantidade_de_alunos_contaminados_por_turma_e_semestre(Aluno, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(confirmado(Aluno))), Contador).
	
busca_alunos_contaminados_por_turma_e_cidade(Aluno, Turma, Cidade) :-
	fact(aluno(Aluno)), fact(aluno_turma(Aluno, Turma)), fact(aluno_cidade(Aluno, Cidade)), fact(confirmado(Aluno)).
	
busca_alunos_contaminados_por_veiculo(Aluno, Veiculo) :-
	fact(aluno(Aluno)), fact(confirmado(Aluno)), fact(aluno_transporte(Aluno, Veiculo)).

%Alunos suspeitos	
busca_alunos_suspeitos_por_turma_e_semestre(Aluno, Turma, Semestre) :- 
	fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(suspeito(Aluno)).
	
busca_quantidade_de_alunos_suspeitos_por_turma_e_semestre(Aluno, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(suspeito(Aluno))), Contador).
	
busca_alunos_suspeitos_por_turma_e_cidade(Aluno, Turma, Cidade) :-
	fact(aluno(Aluno)), fact(aluno_turma(Aluno, Turma)), fact(aluno_cidade(Aluno, Cidade)), fact(suspeito(Aluno)).
	
busca_alunos_suspeitos_por_veiculo(Aluno, Veiculo) :-
	fact(aluno(Aluno)), fact(suspeito(Aluno)), fact(aluno_transporte(Aluno, Veiculo)).

%Alunos mortos
busca_alunos_mortos_por_turma_e_semestre(Aluno, Turma, Semestre) :- 
	fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(morte(Aluno)).
	
busca_quantidade_de_alunos_mortos_por_turma_e_semestre(Aluno, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(aluno(Aluno)), fact(aluno_turma(Aluno,Turma)), fact(aluno_semestre(Aluno, Semestre)), fact(morte(Aluno))), Contador).
	
busca_alunos_mortos_por_turma_e_cidade(Aluno, Turma, Cidade) :-
	fact(aluno(Aluno)), fact(aluno_turma(Aluno, Turma)), fact(aluno_cidade(Aluno, Cidade)), fact(morte(Aluno)).
	
busca_alunos_mortos_por_veiculo(Aluno, Veiculo) :-
	fact(aluno(Aluno)), fact(morte(Aluno)), fact(aluno_transporte(Aluno, Veiculo)).
	
%Professores contaminados
busca_professores_contaminados_por_turma_e_semestre(Professor, Turma, Semestre) :- 
	fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(confirmado(Professor)).
	
busca_quantidade_de_professores_contaminados_por_turma_e_semestre(Professor, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(confirmado(Professor))), Contador).
	
busca_professores_contaminados_por_turma_e_cidade(Professor, Turma, Cidade) :-
	fact(professor(Professor)), fact(professor_turma(Professor, Turma)), fact(professor_cidade(Professor, Cidade)), fact(confirmado(Professor)).
	
busca_professores_contaminados_por_veiculo(Professor, Veiculo) :-
	fact(professor(Professor)), fact(confirmado(Professor)), fact(professor_transporte(Professor, Veiculo)).

%Professores suspeitos
busca_professores_suspeitos_por_turma_e_semestre(Professor, Turma, Semestre) :- 
	fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(suspeito(Professor)).
	
busca_quantidade_de_professores_suspeitos_por_turma_e_semestre(Professor, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(suspeito(Professor))), Contador).
	
busca_professores_suspeitos_por_turma_e_cidade(Professor, Turma, Cidade) :-
	fact(professor(Professor)), fact(professor_turma(Professor, Turma)), fact(professor_cidade(Professor, Cidade)), fact(suspeito(Professor)).
	
busca_professores_suspeitos_por_veiculo(Professor, Veiculo) :-
	fact(professor(Professor)), fact(suspeito(Professor)), fact(professor_transporte(Professor, Veiculo)).

%Professores mortos
busca_professores_mortos_por_turma_e_semestre(Professor, Turma, Semestre) :- 
	fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(morte(Professor)).
	
busca_quantidade_de_professores_mortos_por_turma_e_semestre(Professor, Turma, Semestre, Contador) :-
	aggregate_all(count, (fact(professor(Professor)), fact(professor_turma(Professor,Turma)), fact(professor_semestre(Professor, Semestre)), fact(morte(Professor))), Contador).
	
busca_professores_mortos_por_turma_e_cidade(Professor, Turma, Cidade) :-
	fact(professor(Professor)), fact(professor_turma(Professor, Turma)), fact(professor_cidade(Professor, Cidade)), fact(morte(Professor)).
	
busca_professores_mortos_por_veiculo(Professor, Veiculo) :-
	fact(professor(Professor)), fact(morte(Professor)), fact(professor_transporte(Professor, Veiculo)).

atualizar_pessoa_para_confirmada(Pessoa) :-
	fact(suspeito(Pessoa)) ->
	retract_fact(suspeito(Pessoa)),
	print("suspeito"),
	assert_fact(confirmado(Pessoa))
	; fact(confirmado(Pessoa)) ->
	retract_fact(confirmado(Pessoa)),
	print("confirmado"),
	assert_fact(confirmado(Pessoa))
	; fact(morte(Pessoa))  ->
	retract_fact(morte(Pessoa)),
	print("morte"),
	assert_fact(confirmado(Pessoa))
	; assert_fact(confirmado(Pessoa)).

atualizar_pessoa_para_suspeita(Pessoa) :-
	fact(suspeito(Pessoa)) ->
	retract_fact(suspeito(Pessoa)),
	assert_fact(suspeito(Pessoa))
	; fact(confirmado(Pessoa)) ->
	retract_fact(confirmado(Pessoa)),
	assert_fact(suspeito(Pessoa))
	; fact(morte(Pessoa))  ->
	retract_fact(morte(Pessoa)),
	assert_fact(suspeito(Pessoa))
	; assert_fact(suspeito(Pessoa)).

atualizar_pessoa_para_morta(Pessoa) :-
	fact(suspeito(Pessoa)) ->
	retract_fact(suspeito(Pessoa)),
	assert_fact(morte(Pessoa))
	; fact(confirmado(Pessoa)) ->
	retract_fact(confirmado(Pessoa)),
	assert_fact(morte(Pessoa))
	; fact(morte(Pessoa))  ->
	retract_fact(morte(Pessoa)),
	assert_fact(morte(Pessoa))
	; assert_fact(morte(Pessoa)).

atualizar_pessoa_para_nao_infectada(Pessoa) :-
	fact(suspeito(Pessoa)) ->
	retract_fact(suspeito(Pessoa))
	; fact(confirmado(Pessoa)) ->
	retract_fact(confirmado(Pessoa))
	; fact(morte(Pessoa))  ->
	retract_fact(morte(Pessoa)).

% regras para recuperar quantidades por status
busca_quantidade_alunos_confirmados(X, Confirmados) :-
	aggregate_all(count, (fact(aluno(X)),fact(confirmado(X))), Confirmados).

busca_quantidade_alunos_suspeitos(X, Suspeitas) :-
    aggregate_all(count, (fact(aluno(X)), fact(suspeito(X))), Suspeitas).

busca_quantidade_alunos_mortos(X, Mortes) :-
    aggregate_all(count, (fact(aluno(X)), fact(morte(X))), Mortes).

busca_quantidade_de_alunos_nao_contaminadas(Pessoa, NaoContaminados) :-
    aggregate_all(count, (fact(aluno(Pessoa)), \+fact(confirmado(Pessoa)), \+fact(suspeito(Pessoa)), \+fact(morte(Pessoa))), NaoContaminados).

busca_quantidade_professores_confirmados(X, Confirmados) :-
	aggregate_all(count, (fact(professor(X)),fact(confirmado(X))), Confirmados).

busca_quantidade_professores_suspeitos(X, Suspeitas) :-
    aggregate_all(count, (fact(professor(X)), fact(suspeito(X))), Suspeitas).

busca_quantidade_professores_mortos(X, Mortes) :-
    aggregate_all(count, (fact(professor(X)), fact(morte(X))), Mortes).

busca_quantidade_de_professores_nao_contaminadas(Pessoa, NaoContaminados) :-
    aggregate_all(count, (fact(professor(Pessoa)), \+fact(confirmado(Pessoa)), \+fact(suspeito(Pessoa)), \+fact(morte(Pessoa))), NaoContaminados).

busca_alunos_parentes_de_outro_aluno_infectado(Aluno, Parente) :-
	fact(aluno(Aluno)), fact(confirmado(Aluno)), fact(parente(Aluno, Parente)), fact(aluno(Parente)).

busca_professores_parentes_de_outro_professor_infectado(Professor, Parente) :-
	fact(professor(Professor)), fact(confirmado(Professor)), fact(parente(Professor, Parente)), fact(professor(Parente)).

fact --> { fact(fact, Fact1) }, [Fact1].
