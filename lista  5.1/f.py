def fib(numero):
  N=int(input(numero))
  cont=10
  if N<=1:
    return N
  
  while cont > N:
    return fib(N-1) + fib(N-2)
   


