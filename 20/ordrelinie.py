class ordrelinie :
	def __init__(x,id,navn,pris,antal) :
		x.id = id
		x.navn = navn
		x.pris = eval(pris)
		x.antal = eval(antal)
	def vis(x) :
		return str(x.antal)+" "+x.id+" "+x.navn+" "+str(x.pris)+" "+str(x.pris*x.antal)
