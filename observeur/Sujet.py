from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from Observateur import Observateur

class Sujet(ABC):

    _observateur: List[Observateur] = []

    def abonner(self,observateur:Observateur):
        self._observateur.append(observateur)
        print("One attachement created")

    
    def desabonner(self,observateur:Observateur):
        self._observateur.remove(observateur)

    def notifier(self) -> None:
        for observeur in self._observateur:
            observeur.miseAjour()