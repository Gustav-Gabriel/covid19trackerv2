:- module(pengineService,
    [ add_data_base_values/1
    , confirmed_cases_amount/2
    , suspicious_cases_amount/2
    , deaths_amount/2
    ]
).

:- use_module(library(persistency)).
:- use_module(library(http/json)).

:- persistent fact(fact1:any).

:- db_attach('v2_db.pl', []).

add_all_facts([]).
add_all_facts([X|Rest]) :- assert_fact(X), nl, print(X), nl, add_all_facts(Rest).

add_data_base_values(Json) :- 
%insert people
    atom_json_dict(Json, PeopleDict, [default_tag(person)]),
    dicts_to_compounds(PeopleDict.object.people, [name], dict_fill(null), People),
    add_all_facts(People),

% insert relatives    
    atom_json_dict(Json, RelativesDict, [default_tag(relative)]),
    dicts_to_compounds(RelativesDict.object.relatives, [parent1, parent2], dict_fill(null), Relatives),
    add_all_facts(Relatives),

% insert students
    atom_json_dict(Json, StudentsDict, [default_tag(student)]),
    dicts_to_compounds(StudentsDict.object.students, [name, course, grade], dict_fill(null), Students),
    add_all_facts(Students),

% insert professors
    atom_json_dict(Json, ProfessorsDict, [default_tag(professor)]),
    dicts_to_compounds(ProfessorsDict.object.professors, [name, course, grade], dict_fill(null), Professors),
    add_all_facts(Professors),

% insert confirmed cases
    atom_json_dict(Json, ConfirmedCasesDict, [default_tag(confirmed)]),
    dicts_to_compounds(ConfirmedCasesDict.object.confirmed, [name], dict_fill(null), ConfimedCases),
    add_all_facts(ConfimedCases),

% insert deaths
    atom_json_dict(Json, DeathCasesDict, [default_tag(dead)]),
    dicts_to_compounds(DeathCasesDict.object.deaths, [name], dict_fill(null), DeathCases),
    add_all_facts(DeathCases),

% insert suspicious cases
    atom_json_dict(Json, SuspiciousCasesDict, [default_tag(suspicious)]),
    dicts_to_compounds(SuspiciousCasesDict.object.suspicious, [name], dict_fill(null), SuspiciousCases),
    add_all_facts(SuspiciousCases).


%REGRAS_PARA_BUSCAR_QUANTIDADES

confirmed_cases_amount(X, Counter):-
    aggregate_all(count, fact(confirmed(X)), Counter).

suspicious_cases_amount(X, Counter):-
    aggregate_all(count, fact(suspicious(X)), Counter).

deaths_amount(X, Counter):-
    aggregate_all(count, fact(dead(X)), Counter).

fact --> { fact(fact, Fact1) }, [Fact1].