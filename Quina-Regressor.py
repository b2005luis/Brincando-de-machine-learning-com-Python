from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPRegressor

from QuinaRepository import QuinaRepository

repository = QuinaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Ganhadores")
repository.finalizar()

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4]]
y_axis = data[5]

regressor = MLPRegressor(hidden_layer_sizes=(30))

ex = 25
ks = y_axis.__len__() - ex

regressor.fit(x_axis, y_axis)

print("Esperados")
esperados = x_axis[ks:]
print("{}\n".format(esperados))

acertos = []
apostas = []

lista = list(range(1, 81, 1))

i = 1
while i <= 10:
    to_predict = sample(lista, 5)

    predicted = regressor.predict([to_predict])

    if predicted >= 0.0625:
        for ix, row in esperados.iterrows():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)
                if acertos.__len__() > 2:
                    break

        if acertos.__len__() <= 2:
            aposta = sorted(to_predict, reverse=False)
            apostas.append(aposta)
            i = i + 1
        acertos.clear()

# print("\n{}".format(apostas))
print("\n[")
for jogo in apostas.__iter__():
    print("   {}".format(jogo))
print("]")
