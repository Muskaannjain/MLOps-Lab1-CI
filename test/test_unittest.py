import unittest
from src.metrics import accuracy, precision, recall, f1_score


class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.y_true = [1, 0, 1, 1]
        self.y_pred = [1, 0, 0, 1]

    def test_accuracy(self):
        self.assertAlmostEqual(accuracy(self.y_true, self.y_pred), 0.75)

    def test_precision(self):
        self.assertAlmostEqual(precision(self.y_true, self.y_pred), 1.0)

    def test_recall(self):
        self.assertAlmostEqual(recall(self.y_true, self.y_pred), 2 / 3)

    def test_f1_score(self):
        self.assertAlmostEqual(f1_score(self.y_true, self.y_pred), 0.8)

    def test_empty_lists_raise_error(self):
        for func in [accuracy, precision, recall, f1_score]:
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func([], [])

    def test_different_lengths_raise_error(self):
        for func in [accuracy, precision, recall, f1_score]:
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func([1, 0, 1], [1, 0])


if __name__ == "__main__":
    unittest.main()