import sqlite3
from sqlite3 import Connection, Cursor


class MegaSenaRepository:
    connect: Connection
    cursor: Cursor

    def __init__(self):
        self.connect = sqlite3.connect("./Dados/Mega-Sena.db")
        self.cursor = self.connect.cursor()

    def existe(self, params: any):
        result_set = None
        if type(self.connect) == Connection:
            try:
                self.cursor.execute("SELECT * FROM Resultados WHERE Concurso = ?", params)
                result_set = self.cursor.fetchone()
            except Exception as erro:
                print(erro.__str__())

            return result_set

    def listar_resultados(self, colunas: str):
        results = []
        try:
            self.cursor.execute("SELECT {} FROM Resultados".format(colunas))
            results = self.cursor.fetchall()
        except Exception as erro:
            print(erro.__str__())

        return results

    def cadastrar(self, params: any):
        try:
            self.cursor.execute(
                "INSERT INTO Resultados VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                params
            )
            self.connect.commit()
        except Exception as erro:
            print(erro.__str__())

    def finalizar(self):
        self.cursor.close()
        self.connect.close()
