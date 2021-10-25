
from abc import abstractmethod
from Observateur import Observateur
from Sujet import Sujet
from SujetConcret import SujetConcret


class ObservateurConcret(Observateur):

    _sujet: SujetConcret
    _temperature:int


    def __init__(self, suj:Sujet):
        self._sujet=suj
        print("Creating a instance of ObservateurConcret")


    
    def miseAjour(self) -> None:
	    self._temperature = self._sujet.getA()
	    print("j ai ete mise a jour moi ObservateurConcrete")
	
	
    def getTemperature(self) -> int:
	    return self._temperature
	