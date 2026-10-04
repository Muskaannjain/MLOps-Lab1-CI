import pytest
from src.metrics import accuracy, precision, recall, f1_score

Y_TRUE = [1, 0, 1, 1]
Y_PRED = [1, 0, 0, 1]


def test_accuracy():
    assert accuracy(Y_TRUE, Y_PRED) == pytest.approx(0.75)


def test_precision():
    assert precision(Y_TRUE, Y_PRED) == pytest.approx(1.0)


def test_recall():
    assert recall(Y_TRUE, Y_PRED) == pytest.approx(2 / 3)


def test_f1_score():
    assert f1_score(Y_TRUE, Y_PRED) == pytest.approx(0.8)


@pytest.mark.parametrize(
    "y_true, y_pred, expected",
    [
        ([1, 1, 1], [1, 1, 1], 1.0),
        ([0, 0, 0], [1, 1, 1], 0.0),
        ([1, 0], [1, 1], 0.5),
    ],
)
def test_accuracy_many_cases(y_true, y_pred, expected):
    assert accuracy(y_true, y_pred) == pytest.approx(expected)


def test_no_positive_guesses():
    assert precision([1, 0], [0, 0]) == 0.0
    assert f1_score([1, 1], [0, 0]) == 0.0


def test_no_actual_positives():
    assert recall([0, 0], [1, 0]) == 0.0


@pytest.mark.parametrize("func", [accuracy, precision, recall, f1_score])
def test_empty_lists_raise_error(func):
    with pytest.raises(ValueError):
        func([], [])


@pytest.mark.parametrize("func", [accuracy, precision, recall, f1_score])
def test_different_lengths_raise_error(func):
    with pytest.raises(ValueError):
        func([1, 0, 1], [1, 0])