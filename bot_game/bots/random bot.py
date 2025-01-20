import random


def decision_function(history: list[bool]) -> bool:
    """
    Given the name of the current opponent and previous match history, this function needs to return whether to co-operate or not.
    :param history: A list of match history of whether they co-operated or not so far.
    :return: Should the bot co-operate or not
    """
    decision = bool(random.randint(0, 1))
    # Write Your code here

    ...
    return decision
