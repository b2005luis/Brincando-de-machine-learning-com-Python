from random import sample

from pandas import DataFrame
from sklearn.neural_network import MLPClassifier

from MegaSenaRepository import MegaSenaRepository

repository = MegaSenaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5]]
y_axis = data[6]

classifier = MLPClassifier(hidden_layer_sizes=(60,60))

ex = 8
ks = y_axis.__len__() - ex

classifier.fit(x_axis, y_axis)

print("Esoerados")
esperados = x_axis[ks:]
print("{}\n".format(esperados))

acertos = []
apostas = []

# Lista completa de numeros
lista = list(range(1, 61, 1))

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = classifier.predict([to_predict])

    if predicted <= [0]:
        for ix, row in esperados.iterrows():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)

        if acertos.__len__() <= 3:
            aposta = sorted(to_predict, reverse=False)
            apostas.append(aposta)
            print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
            i = i + 1
        acertos.clear()

print("\n{}".format(apostas))
