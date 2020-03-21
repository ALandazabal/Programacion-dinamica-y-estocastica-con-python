import time
import sys

def fibonacci_recursivo(n):
    if n ==0 or n==1:
        return 1

    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memo={}):
	if n==0 or n==1:
		return 1

	try:
		return memo[n]
	except KeyError:
		resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
		memo[n] = resultado

		return resultado

if __name__=="__main__":
	sys.setrecursionlimit(10002) #Para configurar el límite de recursión
    
	n = int(input('Escoge un numero:'))

	tic = time.process_time()
	#res = fibonacci_recursivo(n)
	res = fibonacci_dinamico(n)
	toc = time.process_time()
	print(res)
	print('Fibonacci {}'.format(str(n))+ '\n... tiempo de calculo '+ str((toc-tic)*1000)+ 'ms')