from datetime import date
from typing import Iterable, Dict
from matchpredictor.matchresults.result import Fixture, Outcome, Result
from matchpredictor.predictors.predictor import Prediction, Predictor


class SpiTable:
    def __init__(self) -> None:
        self.match_date_dict: Dict[str, date] = {}
        self.spi_dict: Dict[str, float] = {}

    def record(self, result: Result) -> None:
        home_team = result.fixture.home_team.name
        home_spi = result.home_spi
        away_team = result.fixture.away_team.name
        away_spi = result.away_spi
        match_date = result.match_date

        if home_team not in self.match_date_dict or self.match_date_dict[home_team] < match_date:
            self.match_date_dict[home_team] = match_date
            self.spi_dict[home_team] = home_spi

        if away_team not in self.match_date_dict or self.match_date_dict[away_team] < match_date:
            self.match_date_dict[away_team] = match_date
            self.spi_dict[away_team] = away_spi

    def predict(self, fixture: Fixture) -> Prediction:
        if fixture.home_team.name not in self.spi_dict or fixture.away_team.name not in self.spi_dict:
            return Prediction(Outcome.HOME)
        if self.spi_dict[fixture.home_team.name] > self.spi_dict[fixture.away_team.name]:
            return Prediction(Outcome.HOME)
        else:
            return Prediction(Outcome.AWAY)

class LatestSpiPredictor(Predictor):
    def __init__(self, spi_table: SpiTable) -> None:
        self.spi_table = spi_table

    def predict(self, fixture: Fixture) -> Prediction:
        return self.spi_table.predict(fixture)

def get_latest_spis(results: Iterable[Result]) -> Predictor:
    return LatestSpiPredictor(calculate_spi(results))

def calculate_spi(results: Iterable[Result]) -> SpiTable:
    table = SpiTable()

    for result in results:
        table.record(result)

    return table