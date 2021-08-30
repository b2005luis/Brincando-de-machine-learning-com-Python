from MegaSenaDownload import MegaSenaDownload
from MegaSenaRepository import MegaSenaRepository

download = MegaSenaDownload()
download.buscar_resultados()

repository = MegaSenaRepository()

for item in download.data:
    concurso = item[0]
    if not repository.existe([concurso]):
        print(item)
        repository.cadastrar(item)

repository.finalizar()