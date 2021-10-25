from abc import ABC, abstractmethod


class Observateur(ABC):
    
    @property
    @abstractmethod
    def miseAjour()->None:
        pass