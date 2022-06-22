from pandas import DataFrame


class Loteria:
    bets: list
    candidate_bet: list
    max_numbers: int
    max_bets: int
    dataset: DataFrame

    def __init__(self, max_numbers: int = 6, max_bets: int = 7):
        self.candidate_bet = []
        self.bets = []
        self.max_numbers = max_numbers
        self.max_bets = max_bets

    def generate_bet(self, start: int = 1, end: int = 60):
        self.candidate_bet = list(range(1, (end + 1), 1))
        return self.candidate_bet

    def set_dataset(self, dataset: DataFrame):
        self.dataset = dataset
