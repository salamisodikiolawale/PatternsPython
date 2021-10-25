
from Sujet import Sujet


class SujetConcret(Sujet):

	_a: int
	
	def __init__(self) -> None:
		super().__init__()
	
	def opVisible(self) -> None:
		print("Operation important")
		self.notifier()
	

	def addtion(self) -> None:
		self._a += 1
		self.notifier()
	
	def getA(self) -> int: 
		return 1 #self._a