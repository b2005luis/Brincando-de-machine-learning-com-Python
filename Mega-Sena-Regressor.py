from random import sample

import pandas
from sklearn.neural_network import MLPRegressor

data = pandas.read_csv("../mega-sena.csv", header=0, sep=";")
x_axis = data[["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", "Coluna 5", "Coluna 6"]]
y_axis = data["Ganhadores Faixa 1"]

regressor = MLPRegressor(hidden_layer_sizes=(24, 24),
                         learning_rate="adaptive")
regressor.best_validation_score_ = 0.66

k = y_axis.__len__() - 30
lista = []
for ix, row in x_axis[k:].iterrows():
    for item in row:
        if not lista.__contains__(item):
            lista.append(item)

regressor.fit(x_axis, y_axis)

i = 1
while i <= 7:
    to_predict = sample(lista, 6)
    predicted = regressor.predict([to_predict])
    if predicted >= 1.0:
        print("{} :: {}".format(sorted(to_predict, reverse=False), predicted))
        i = i + 1