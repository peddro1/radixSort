from random import shuffle
import random
import math
import timeit
import matplotlib.pyplot as plt


timeRadix = []
elementos = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]

def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def radixSort(lista):
    RADIX = 10
    maxLength = False
    tmp = -1
    placement = 1
  
    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range( RADIX )]
  
        for i in lista:
            tmp = i // placement
            buckets[tmp % RADIX].append( i )
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                lista[a] = i
                a += 1
    
        placement *= RADIX



def timePopulate():
	for numElementos in elementos:
		base = []
		base = geraLista(numElementos)

	
		_tmp = list(base)
		timeRadix.append(timeit.timeit("radixSort({})".format(_tmp), \
        setup="from __main__ import radixSort", \
        number=1))
		

def axis():
	timePopulate()

	
	plt.plot(elementos, timeRadix, label="RadixSort")
  
def graphic():
	plt.legend(loc='upper center', shadow=True).get_frame().set_facecolor('0.90')
	plt.xlabel('Tamanho(int)')
	plt.ylabel('Tempo(s)')
	plt.show()

def main():
	axis()
	graphic()

if __name__ == "__main__":
	main()
