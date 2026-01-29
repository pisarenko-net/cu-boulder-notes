from unittest import TestCase

from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.matchresults.results_provider import training_results, validation_results
from matchpredictor.predictors.spi_predictor import get_latest_spis
from test.predictors import csv_location


class TestSpiPredictor(TestCase):
    def test_accuracy(self) -> None:
        training_data = training_results(csv_location, 2022)
        validation_data = validation_results(csv_location, 2022)

        predictor = get_latest_spis(training_data)
        accuracy, _ = Evaluator(predictor).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .45)
