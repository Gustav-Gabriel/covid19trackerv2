:- module(pengines_server,
    [ serve/1
    , serve/0
    ]).

% Web Server
:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/json)).

serve(Port) :-
    http_server(http_dispatch, [port(Port)]).

serve :-
    serve(5051).

% File paths
:- dynamic user:file_search_path/2.
:- prolog_load_context(directory, Dir),
   asserta(user:file_search_path(app, Dir)).

% Pengines: register app
:- use_module(library(pengines)).
:- pengine_application(virus).
:- use_module(virus:app(pengineService)).



% Sandbox the predicates deemed unsafe due to using a mutex.
:- use_module(library(sandbox)).
:- multifile sandbox:safe_primitive/1.
sandbox:safe_primitive(pengineService:inserir_parentes(_)).
sandbox:safe_primitive(pengineService:inserir_professores(_)).
sandbox:safe_primitive(pengineService:inserir_alunos(_)).
sandbox:safe_primitive(pengineService:inserir_casos_confirmados(_)).
sandbox:safe_primitive(pengineService:inserir_casos_suspeitos(_)).
sandbox:safe_primitive(pengineService:inserir_casos_morte(_)).
sandbox:safe_primitive(pengineService:busca_quantidade_casos_confirmados(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_casos_suspeitos(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_casos_morte(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_pessoas_nao_contaminadas(_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_contaminados_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_alunos_contaminados_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_contaminados_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_contaminados_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_suspeitos_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_alunos_suspeitos_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_suspeitos_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_suspeitos_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_mortos_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_alunos_mortos_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_mortos_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_alunos_mortos_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_professores_contaminados_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_professores_contaminados_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_contaminados_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_contaminados_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_professores_suspeitos_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_professores_suspeitos_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_suspeitos_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_suspeitos_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_professores_mortos_por_turma_e_semestre(_,_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_professores_mortos_por_turma_e_semestre(_,_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_mortos_por_turma_e_cidade(_,_,_)).
sandbox:safe_primitive(pengineService:busca_professores_mortos_por_veiculo(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_alunos_confirmados(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_alunos_suspeitos(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_alunos_mortos(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_alunos_nao_contaminadas(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_professores_confirmados(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_professores_suspeitos(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_professores_mortos(_,_)).
sandbox:safe_primitive(pengineService:busca_quantidade_de_professores_nao_contaminadas(_,_)).
sandbox:safe_primitive(pengineService:atualizar_pessoa_para_confirmada(_)).
sandbox:safe_primitive(pengineService:atualizar_pessoa_para_suspeita(_)).
sandbox:safe_primitive(pengineService:atualizar_pessoa_para_morta(_)).
sandbox:safe_primitive(pengineService:atualizar_pessoa_para_nao_infectada(_)).
sandbox:safe_primitive(pengineService:busca_alunos_parentes_de_outro_aluno_infectado(_,_)).
sandbox:safe_primitive(pengineService:busca_professores_parentes_de_outro_professor_infectado(_,_)).
