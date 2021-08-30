from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPClassifier

from MegaSenaRepository import MegaSenaRepository

repository = MegaSenaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5]]
y_axis = data[6]

classifier = MLPClassifier(hidden_layer_sizes=(30, 30),
                           alpha=0.0,
                           beta_1=0.0,
                           beta_2=0.0,
                           learning_rate="adaptive")

ex = 8
ks = y_axis.__len__() - ex
ke = y_axis.__len__()
lista = []
for ix, row in x_axis[ks:ke].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

classifier.fit(x_axis[:ks], y_axis[:ks])

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = classifier.predict([to_predict])
    if predicted >= 1:
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        i = i + 1
