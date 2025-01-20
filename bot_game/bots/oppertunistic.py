import random

def decision_function(history):
    if not len(history[1]):
        return True
    last = history[1][-1]
    if last:
        return bool(random.randint(0, 9))
    return False
