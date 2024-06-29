import matplotlib.pyplot as plt



plt.title ('Testando Gráficos')
labels = ['a','b', 'c', 'd', 'e', 'f', 'g' ]
frequencia = [1,56,56,19,9,9,8]
frequencia.sort()

plt.pie (frequencia)


plt.grid(True)
plt.show()
