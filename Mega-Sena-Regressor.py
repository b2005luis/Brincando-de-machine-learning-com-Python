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

regressor = MLPRegressor(hidden_layer_sizes=(30, 30),
                         alpha=0.0,
                         beta_1=0.0,
                         beta_2=0.0,
                         learning_rate="adaptive")

ks = y_axis.__len__() - 20
ke = y_axis.__len__() - 2
lista = []
for ix, row in x_axis[ks:ke].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

regressor.fit(x_axis, y_axis)

print("Esoerados")
esperados = x_axis[x_axis.__len__() - 1:]
print("{}\n".format(esperados))

acertos = []

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = regressor.predict([to_predict])
    if predicted >= 0.0666666666666667 and predicted <= 0.1:
        for ix, row in esperados.iterrows():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        print("Acerto(s) :: {} = {} acertos".format(acertos, acertos.__len__()))
        i = i + 1
        acertos.clear()
