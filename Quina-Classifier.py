from random import sample

import pandas
from sklearn.neural_network import MLPClassifier

data = pandas.read_csv("./../quina.csv", header=0, sep=";")
x_axis = data[["1a", "2a", "3a", "4a", "5a"]]
y_axis = data["Gan."]

classifier = MLPClassifier(hidden_layer_sizes=(60,60),
                          learning_rate="adaptive")
classifier.best_validation_score_ = 0.66

k = y_axis.__len__() - 30
lista = []
for ix, row in x_axis[k:].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

classifier.fit(x_axis, y_axis)

i = 1
while i <= 7:
    to_predict = sample(lista, 5)
    predicted = classifier.predict([to_predict])
    if predicted > 0:
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        i = i + 1
