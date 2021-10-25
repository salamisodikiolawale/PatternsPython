from ObservateurConcret import ObservateurConcret
from SujetConcret import SujetConcret


if __name__ == "__main__":
    
    sjc = SujetConcret()
		
	#Creating Observateurs
    obs1 = ObservateurConcret(sjc)
    obs2 = ObservateurConcret(sjc)
		
	#Abonnement
    sjc.abonner(obs1)
    sjc.abonner(obs2)

	# #
    sjc.opVisible()
    # sjc.desabonner(obs2)
    # sjc.opVisible()
		
	# #Incrementation de a 
    # sjc.addtion()
    # sjc.addtion()
    
    # print(obs1.getTemperature())