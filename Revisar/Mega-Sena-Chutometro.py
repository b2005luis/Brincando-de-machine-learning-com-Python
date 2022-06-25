from random import sample
from pandas import DataFrame
from MegaSenaRepository import QuinaRepository


repository = QuinaRepository()
download = repository.listar_resultados("Coluna1, Coluna2, Coluna3, Coluna4, Coluna5, Coluna6, Ganhadores")
repository.finalizar()

data = DataFrame(download)

x_axis = data[[0, 1, 2, 3, 4, 5]]
y_axis = data[6]

ex = y_axis.__len__()
ks = y_axis.__len__() - ex

print("Esperados")
esperados = x_axis[ks:]
print("{}\n".format(esperados))

lista = list(range(1, 61, 1))
acertos = []
apostas = []

i = 1
while i <= 7:
    chute = sample(lista, 6)
    to_predict = sorted(chute, reverse=False)

    for ix, row in esperados.iterrows():
        for e in row.__iter__():
            if to_predict.__contains__(e):
                acertos.append(e)
        if acertos.__len__() >= 3:
            break

    print("{} :: Acertos: {} acertos".format(to_predict, acertos.__len__()))

    if acertos.__len__() <= 3:
        aposta = sorted(to_predict, reverse=False)
        apostas.append(aposta)
        esperados.__add__(to_predict)
        i = i + 1

    acertos.clear()


# print("\n{}".format(apostas))
print("\n[")
for jogo in apostas.__iter__():
    print("   {}".format(jogo))
print("]")
