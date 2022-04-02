from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPRegressor

from MegaSenaRepository import MegaSenaRepository

repository = MegaSenaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")
repository.finalizar()

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5]]
y_axis = data[6]

regressor = MLPRegressor(hidden_layer_sizes=(60, 60))

ex = 30
ks = y_axis.__len__() - ex

regressor.fit(x_axis, y_axis)

print("Esperados")
esperados = x_axis[ks:]
print("{}\n".format(esperados))

acertos = []
apostas = []

lista = list(range(1, 61, 1))

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = regressor.predict([to_predict])

    if predicted >= [2.0]:
        for ix, row in esperados.iterrows():
            for e in row.__iter__():
                if to_predict.__contains__(e):
                    acertos.append(e)
            if acertos.__len__() > 1:
                break
            acertos.clear()

        print("{} :: Acertos: {} acertos".format(to_predict, acertos.__len__()))

        if acertos.__len__() <= 1:
            aposta = sorted(to_predict, reverse=False)
            apostas.append(aposta)
            i = i + 1
        esperados.__add__(to_predict)
        acertos.clear()


print("\n[")
for jogo in apostas.__iter__():
    print("   {}".format(jogo))
print("]")
'''
to_predict = [9, 14, 22, 24, 44, 47]
predicted = regressor.predict([to_predict])
print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
'''
