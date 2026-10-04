def _check_inputs(y_true, y_pred):
    """Make sure the two lists can be compared."""
    if len(y_true) == 0:
        raise ValueError("Inputs cannot be empty.")
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length.")


def accuracy(y_true, y_pred):
    """Fraction of guesses that were correct."""
    _check_inputs(y_true, y_pred)
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)


def precision(y_true, y_pred):
    """When the model guessed 1, how often was it really 1."""
    _check_inputs(y_true, y_pred)
    true_pos = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    guessed_pos = sum(1 for p in y_pred if p == 1)
    if guessed_pos == 0:
        return 0.0
    return true_pos / guessed_pos


def recall(y_true, y_pred):
    """Of all the real 1s, how many did the model catch."""
    _check_inputs(y_true, y_pred)
    true_pos = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    actual_pos = sum(1 for t in y_true if t == 1)
    if actual_pos == 0:
        return 0.0
    return true_pos / actual_pos


def f1_score(y_true, y_pred):
    """One score that balances precision and recall."""
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)