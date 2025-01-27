def decision_function(my_history: list[bool], opponent_history: list[bool]) -> bool:
    """
    Given the previous match history, this function needs to return whether the bot should co-operate or not.
    :param my_history: List of booleans containing your past decisions against the opponent's bot.
    :param opponent_history: List of booleans containing your opponent's past decisions against your bot.
    :return: Should this bot co-operate or defer (True to co-operate, False to defer)?
    """
    if opponent_history:
        return opponent_history[-1]
    return True
