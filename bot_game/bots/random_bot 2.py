import random


def decision_function(history: tuple[list[bool], list[bool]]) -> bool:
    """
    Given the name of the current opponent and previous match history, this function needs to return whether to co-operate or not.
    :param history: A list of match history of whether they co-operated or not so far.
    :return: Should the bot co-operate or not
    """
    decision = not history[1][-1] if history[1] else True
    # Write Your code here

    ...
    return decision
