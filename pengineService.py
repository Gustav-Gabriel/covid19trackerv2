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

    def insertDatabaseThroughJson(self, json):
        print(json)
        pengine = self.new_pengine()
        query = pengine.ask(f"add_data_base_values('{json}')")
        pengine.doAsk(query)
        pengine.iAmFinished(query)

    def getConfirmedCasesAmount(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"confirmed_cases_amount(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def getSuspiciousCasesAmount(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"suspicious_cases_amount(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result

    def getDeathsAmount(self):
        pengine = self.new_pengine()
        query = pengine.ask(f"deaths_amount(X,Counter)")
        pengine.doAsk(query)
        result = pengine.currentQuery.availProofs
        pengine.iAmFinished(query)
        return result