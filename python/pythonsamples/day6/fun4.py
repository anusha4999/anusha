def fun(**kwargs):
	k=kwargs.keys()
	l=kwargs.values()
	h=kwargs.items()
	print(h)
	for i,j in h:
	#for j in l:
	 	print('hello this is {} from {}'.format(key,value))
fun(batman='usa',superman='pk',ironman='ind')
