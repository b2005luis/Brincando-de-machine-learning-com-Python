import requests


class LotofacilDownload():
    endpoint: str
    data: list
    request: None

    def __init__(self):
        self.request = requests
        self.endpoint = "https://redeloteria.com.br/rotinas_06/arquivos_txt/tx_lotofacil_todos_resultados.txt"

    def buscar_resultados(self):
        temp_data = self.request.get(self.endpoint,
                                     headers={"content-type": "application/json"})
        self.data = temp_data.json()["data"]
