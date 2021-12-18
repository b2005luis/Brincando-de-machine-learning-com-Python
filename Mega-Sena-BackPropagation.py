from random import sample

from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised import BackpropTrainer
from pybrain3.tools.shortcuts import buildNetwork

from MegaSenaRepository import MegaSenaRepository

# Load data for trainer and network
repository = MegaSenaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")
repository.finalizar()

# DataSet model.
dataset = SupervisedDataSet(6, 1)
for row in download.__iter__():
    in_value = row[:6]
    out_value = row[6:][0]
    dataset.addSample(in_value, out_value)

# Create neural network
neural = buildNetwork(6, 60, 60, 1, bias=True)

# Train for models
trainer = BackpropTrainer(neural, dataset)
for i in range(11):
    TTR = float(trainer.train())
    print("{}ª Fase do Treinamento | Margem de Erro :: {:.2f}%".format(i, TTR))

# Numbers generator
all_numbers = list(range(1, 61, 1))

ex = 15
k = download.__len__()
# print("\nEsoerados")
esperados = []
for row in download[(k - ex):].__iter__():
    esperados.append(row[:6])
    # print("{}".format(row[:6]))

acertos = []
i = 1
while i <= 14:
    to_predict = sample(all_numbers, 6)

    # Activate network
    predicted = float(neural.activate(to_predict))

    if predicted >= 0.0 and predicted <= TTR:
        for row in esperados.__iter__():
            for e in row:
                if to_predict.__contains__(e):
                    acertos.append(e)
        if len(acertos) <= 1:
            print("\n{} :: {:.2f}".format(sorted(to_predict, reverse=False), predicted))
            print("Acerto(s) :: {} = {} acertos".format(acertos, acertos.__len__()))
            i = i + 1
        acertos.clear()
