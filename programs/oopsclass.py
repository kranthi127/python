class bottle:
	#properties/state
	id=1
	colour="red"
	height=10

	#constructor
	def __init__(self):
	    print('constructor')

	#functions/behavour
	def wash(self):
		print('washing')
	def setcap(self):
		print('setcap')
	def fillwater(self):
		print('fillwater')
#object creation
bottle1 =bottle()   #creation of the object 
print(bottle1)
print(bottle1.colour)
bottle1.wash()



