import time

def fibonacci_recursivo(n):
    if n ==0 or n==1:
        return 1
    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)


if __name__=="__main__":
    n = int(input('Escoge un numero:'))

    tic = time.process_time()
    res = fibonacci_recursivo(n)
    toc = time.process_time()
    print(res)
    print('Fibonacci {}'.format(str(n))+ '\n... tiempo de calculo '+ str((toc-tic)*1000)+ 'ms')