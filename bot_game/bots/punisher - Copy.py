import random

def decision_function(history):
    if not len(history[1]):  # if first turn
        return bool(random.randint(0, 1))  # a random decision
    return history[1][-1]  # opponent's most recent pick
