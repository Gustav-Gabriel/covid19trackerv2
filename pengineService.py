from pengines.Builder import PengineBuilder
from pengines.Pengine import Pengine

class PengineService:
    """	Constructor
        (must start prolog server separately before)
        Initialize pengine server comunication
    """
    def __init__(self):
        self.pengine_builder = PengineBuilder(urlserver="http://localhost:5051", application="virus")

    def new_pengine(self) :
        return Pengine(builder=self.pengine_builder)

    def inserirParentes(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_parentes('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def inserirProfessores(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_professores('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def inserirAlunos(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_alunos('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def inserirCasosConfirmados(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_casos_confirmados('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def inserirCasosDeSuspeita(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_casos_suspeitos('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def inserirCasosDeMorte(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"inserir_casos_morte('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def buscarQuantidadeDeCasosConfirmados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_casos_confirmados(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeDeCasosDeSuspeita(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_casos_suspeitos(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeDeMortos(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_casos_morte(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeDeNaoInfectados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_de_pessoas_nao_contaminadas(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscaAlunosConfirmadosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_alunos_contaminados_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
        	result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeAlunosContaminadosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_alunos_contaminados_por_turma_e_semestre(X,\""+turma+"\","+semestre+", Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscaAlunosContaminadosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_alunos_contaminados_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result


    def buscaAlunosContaminadosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_alunos_contaminados_por_veiculo(X,\""+veiculo+"\")"
        print(question)
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaAlunosSuspeitosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_alunos_suspeitos_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeAlunosSuspeitosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_alunos_suspeitos_por_turma_e_semestre(X,\""+turma+"\","+semestre+",Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscaAlunosSuspeitosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_alunos_suspeitos_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
        	result = []
        pengine.iAmFinished(query)
        return result

    def buscaAlunosSuspeitosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_alunos_suspeitos_por_veiculo(X,\""+veiculo+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaAlunosMortosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_alunos_mortos_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeAlunosMortosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_alunos_mortos_por_turma_e_semestre(X,\""+turma+"\","+semestre+",Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscaAlunosMortosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_alunos_mortos_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaAlunosMortosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_alunos_mortos_por_veiculo(X,\""+veiculo+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaProfessoresContaminadosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_professores_contaminados_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeProfessoresContaminadosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_professores_contaminados_por_turma_e_semestre(X,\""+turma+"\","+semestre+",Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result
    
    def buscaProfessoresContaminadosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_professores_contaminados_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaProfessoresContaminadosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_professores_contaminados_por_veiculo(X,\""+veiculo+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result    

    def buscaProfessoresSuspeitosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_professores_suspeitos_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeProfessoresSuspeitosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_professores_suspeitos_por_turma_e_semestre(X,\""+turma+"\","+semestre+",Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result
    
    def buscaProfessoresSuspeitosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_professores_suspeitos_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaProfessoresSuspeitosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_professores_suspeitos_por_veiculo(X,\""+veiculo+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result  

    def buscaProfessoresMortosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_professores_mortos_por_turma_e_semestre(X,\""+turma+"\","+semestre+")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaQuantidadeDeProfessoresMortosPorTurmaESemestre(self, turma, semestre):
        pengine = self.new_pengine()
        question = "busca_quantidade_de_professores_mortos_por_turma_e_semestre(X,\""+turma+"\","+semestre+",Contador)"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result
    
    def buscaProfessoresMortosPorTurmaECidade(self, turma, cidade):
        pengine = self.new_pengine()
        question = "busca_professores_mortos_por_turma_e_cidade(X,\""+turma+"\",\""+cidade+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result

    def buscaProfessoresMortosPorVeiculo(self, veiculo):
        pengine = self.new_pengine()
        question = "busca_professores_mortos_por_veiculo(X,\""+veiculo+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result 

    def buscarQuantidadeTotalDeAlunosConfirmados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_alunos_confirmados(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeAlunosComSuspeita(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_alunos_suspeitos(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeAlunosMortos(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_alunos_mortos(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeAlunosNaoInfectados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_de_alunos_nao_contaminadas(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeProfessoresConfirmados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_professores_confirmados(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeProfessoresComSuspeita(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_professores_suspeitos(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeProfessoresMortos(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_professores_mortos(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def buscarQuantidadeTotalDeProfessoresNaoInfectados(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"busca_quantidade_de_professores_nao_contaminadas(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def atualizarStatusDaPessoaParaConfirmada(self, nome):
        pengine = self.new_pengine()
        question = "atualizar_pessoa_para_confirmada(\""+nome+"\")"
        print(question)
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def atualizarStatusDaPessoaParaSuspeita(self, nome):
        pengine = self.new_pengine()
        question = "atualizar_pessoa_para_suspeita(\""+nome+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def atualizarStatusDaPessoaParaMorta(self, nome):
        pengine = self.new_pengine()
        question = "atualizar_pessoa_para_morta(\""+nome+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def atualizaStatusDaPessoaParaNaoInfectada(self, nome):
        pengine = self.new_pengine()
        question = "atualizar_pessoa_para_nao_infectada(\""+nome+"\")"
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def buscaAlunosParentesDeUmAlunoInfectado(self, nome):
        pengine = self.new_pengine()
        question = "busca_alunos_parentes_de_outro_aluno_infectado(\""+nome+"\",X)"
        print(question)
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result 
    
    def buscaProfessoresParentesDeUmProfessorInfectado(self, nome):
        pengine = self.new_pengine()
        question = "busca_professores_parentes_de_outro_professor_infectado(\""+nome+"\",X)"
        print(question)
        query = pengine.ask(f"{question}")
        pengine.doAsk(query)
        if pengine.currentQuery:
            result = pengine.currentQuery.availProofs
            while pengine.currentQuery.hasMore:
                pengine.doNext(pengine.currentQuery)
        else:
            result = []
        pengine.iAmFinished(query)
        return result 
