import numpy as np

# array unidimenssional
a = np.array([0, 1, 2, 3])
print(a)

# array bidimensional
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)
print(b.ndim) # numero de dimensões
print(b.shape) # quantas linhas e colunas, respectivamente
print(len(b)) # so da o numero de linhas

c = np.arange(1 , 100, 2) # cria um array, parametos funcionam iguais ao range
print(c)
c = np.arange(10)
print(c)

# parametros: 1=inicio; 2=fim e é incluido, 3= número de elementos que terão
# se incluido, endpoint=False, o fim não é incluido
d = np.linspace(1, 10, 2)
print(d)
d = np.linspace(1, 10, 25)
print(d)
d = np.linspace(1, 10, 25, endpoint=False)
print(d)