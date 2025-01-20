import random

def decision_function(history):
    if not history[1]:
        return True
    if not history[1][-1]:
        return False
    if len(history[1]) > 1:
        if not history[1][-2]:
            return False
        else:
            return True
    return True
