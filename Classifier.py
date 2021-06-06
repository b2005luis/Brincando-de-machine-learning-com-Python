from random import sample

import pandas
from sklearn.neural_network import MLPClassifier

data = pandas.read_csv("mega-sena.csv", header=0, sep=";")
x_axis = data[["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", "Coluna 5", "Coluna 6"]]
y_axis = data["Ganhadores Faixa 1"]

classifier = MLPClassifier(hidden_layer_sizes=(60),
                           activation="identity",
                           alpha=0,
                           beta_1=0,
                           beta_2=0,
                           shuffle=False)

k = y_axis.__len__() - 10
lista = []
for ix, row in x_axis[k:].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

classifier.fit(x_axis, y_axis)

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = classifier.predict([to_predict])
    if predicted > 0:
        classifier.predict_proba(x_axis)
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        i = i + 1
