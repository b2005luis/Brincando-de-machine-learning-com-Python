from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPClassifier

from MegaSenaRepository import MegaSenaRepository

repository = MegaSenaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5]]
y_axis = data[6]

classifier = MLPClassifier(hidden_layer_sizes=(60, 60))

ex = 20
ks = y_axis.__len__() - ex
ke = y_axis.__len__()
lista = []
for ix, row in x_axis[ks:ke].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

classifier.fit(x_axis, y_axis)

print("Esoerados")
esperados = x_axis[ks + 10:]
print("{}\n".format(esperados))

acertos = []

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = classifier.predict([to_predict])
    if predicted >= 1:
        for ix, row in esperados.iterrows():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)
        if len(acertos) <= 1:
            print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
            print("Acerto(s) :: {} = {} acertos".format(acertos, acertos.__len__()))
            i = i + 1
        acertos.clear()
