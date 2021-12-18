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

regressor = MLPRegressor(hidden_layer_sizes=(30, 30))

ex = 50
ks = y_axis.__len__() - ex
ke = y_axis.__len__()
lista = []
for ix, row in x_axis[ks:ke].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

regressor.fit(x_axis, y_axis)

print("Esoerados")
esperados = x_axis[ke - 8:]
print("{}\n".format(esperados))

acertos = []

lista = list(range(1, 61, 1))

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = regressor.predict([to_predict])
    if predicted >= 6.66666666666667:
        for ix, row in esperados.iterrows():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)
        if len(acertos) <= 2:
            print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
            print("Acerto(s) :: {} = {} acertos".format(acertos, acertos.__len__()))
            i = i + 1
        acertos.clear()

'''
to_predict = [7, 29, 38, 40, 44, 52]
predicted = regressor.predict([to_predict])
print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
'''