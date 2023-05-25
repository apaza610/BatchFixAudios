# maneja el file D:/temp.txt como archivo temporal
# para guardar lista de videos editados y por editarse...

import os
import principal
from os.path import exists
TEMPTXT = "D:/temp.txt"
VIDSPATH = "E:/win/Videos/"		# "D:\\09-Dictionary\\"

def anunciar_si_terminado():
	if os.stat(TEMPTXT).st_size == 0:
		import winsound
		winsound.Beep(frequency=2500, duration=1000)

def write_temptxt(lElementos):
	temptxt = open(TEMPTXT, 'w')
	for elemento in lElementos:
		temptxt.write(elemento + "\n")
	temptxt.close()

def read_temptxt():
	with open(TEMPTXT) as temptxt:
		lTmp = temptxt.readlines()
		lTmp = [linea.rstrip() for linea in lTmp]
	return lTmp

def elim_lista_top_elem(lPaths):
	lPaths.pop(0)
	write_temptxt(lPaths)

def bucle_conversor(lElems):
	print(lElems)
	for elem in lElems:
		principal.aplicar_efectos(elem)
		elim_lista_top_elem(lElems)
		anunciar_si_terminado()

def main():
	lMP4s = []
	if exists(TEMPTXT) and os.stat(TEMPTXT).st_size != 0:		#resume from failed convertion
		lMP4s = read_temptxt()
		bucle_conversor(lMP4s)

if __name__ == '__main__':
	main()