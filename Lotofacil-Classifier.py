from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPClassifier

from LotofacilRepository import LotofacilRepository

repository = LotofacilRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, "
                                        "Coluna6, Coluna7, Coluna8, Coluna9, Coluna10, "
                                        "Coluna11, Coluna12, Coluna13, Coluna14, Coluna15, Ganhadores")
repository.finalizar()

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
y_axis = data[15]

classifier = MLPClassifier(hidden_layer_sizes=(30, 100, 30),
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
    to_predict = sample(lista, 15)
    predicted = classifier.predict([to_predict])
    if predicted >= 1:
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        i = i + 1
