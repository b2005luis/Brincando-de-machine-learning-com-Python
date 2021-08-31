from builtins import list

from LotofacilDownload import LotofacilDownload
from LotofacilRepository import LotofacilRepository

download = LotofacilDownload()
download.buscar_resultados()

repository = LotofacilRepository()

i = 1
parcial: list = []
resultados: list = []
for item in download.data:
    if i == 1:
        parcial.append(item[0])
        parcial.append(item[1])
        parcial.append(item[2])
        parcial.append(item[3])
        parcial.append(item[4])
        parcial.append(item[5])
        parcial.append(item[6])
        i += 1
    elif i == 2:
        parcial.append(item[2])
        parcial.append(item[3])
        parcial.append(item[4])
        parcial.append(item[5])
        parcial.append(item[6])
        i += 1
    elif i == 3:
        parcial.append(item[2])
        parcial.append(item[3])
        parcial.append(item[4])
        parcial.append(item[5])
        parcial.append(item[6])
        parcial.append(item[7])
        parcial.append(item[8])
        resultados.append(parcial)
        parcial = []
        i = 1

for item in resultados:
    concurso = item[0]
    if not repository.existe([concurso]):
        repository.cadastrar(item)
        print(item)
