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
sandbox:safe_primitive(pengineService:add_data_base_values(_)).
sandbox:safe_primitive(pengineService:confirmed_cases_amount(_,_)).
sandbox:safe_primitive(pengineService:suspicious_cases_amount(_,_)).
sandbox:safe_primitive(pengineService:deaths_amount(_,_)).