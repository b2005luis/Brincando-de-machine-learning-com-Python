from QuinaDownload import QuinaDownload
from QuinaRepository import QuinaRepository

download = QuinaDownload()
download.buscar_resultados()

repository = QuinaRepository()

for item in download.data:
    concurso = item[0]
    if not repository.existe([concurso]):
        print(item)
        repository.cadastrar(item)

repository.finalizar()