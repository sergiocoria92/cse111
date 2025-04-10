def func1(): #solo se puede acceder a la variable a dentro de la función func1, pero no hace nada
    #no se ejecuta nada
  a = 1

def func2():
  a = 2#variable local
  func1() #no esta afectando a la variable a de la función func2
  return a

a = 0#no afecta a la variable a de la función func2 porque es cero
print(func2()) #se imprime 2 porque la variable a de la función func2 es 2
