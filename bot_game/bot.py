import os
from time import sleep
from typing import Callable
from copy import deepcopy

type History = tuple[list[bool], list[bool]]
type Bot = Callable[[History], bool]
type Results = dict[str, list[int]]

def do_rename(s: str) -> str:
    return s.replace(" ", "").replace("-", "_").replace("(", "_").replace(")", "")


def get_all_bots() -> dict[str, Bot]:
    bots = {}
    path = os.path.join(os.getcwd(), "bots")
    for file in os.listdir(path):
        if not file.endswith(".py"):
            continue
        if " " in file:
            original = os.path.join(path, file)
            new = os.path.join(path, do_rename(file))
            os.rename(original, new)
            file_name = do_rename(file).removesuffix(".py")
            renamed = True
        else:
            file_name = file.removesuffix(".py")
            renamed = False
        print(file_name)
        try:
            exec(f"from {os.path.basename(path)}.{file_name} import decision_function as {file_name}_df")
            k, v = file_name, eval(f"{file_name + '_df'}")
            bots[k] = v
            # print(k)
            if renamed:
                os.rename(new, original)
        except SyntaxError:
            if renamed:
                os.rename(new, original)
    return bots


def handle_scoring(r1: bool, r2: bool, wins: list[int]) -> tuple[int, int] | None:
    win = 5
    draw_coop = 3
    draw_deff = 1
    lose = 0
    match (int(r1), int(r2)):
        case (1, 1):
            return draw_coop, draw_coop
        case (0, 0):
            return draw_deff, draw_deff
        case (1, 0):
            wins[1] += 1
            return lose, win
        case (0, 1):
            wins[0] += 1
            return win, lose
    return None


def add_to_history(history: History, r1: bool, r2: bool) -> None:
    history[0].append(r1)
    history[1].append(r2)


def fight_bots(func1: Bot, func2: Bot, n: int) -> tuple[tuple[int, int], list[int]] | tuple[tuple[int | None, int | None], list[int]]:
    history: History = [], []
    score: tuple[int, int] = 0, 0
    wins: list[int] = [0, 0]
    i: int = 0
    while i < n:
        r1: bool | None = func1(history1)
        r2: bool | None = func2(history2)
        if r1 is None or r2 is None:
            return (r1, r2), wins
        add_to_history(history1, r1, r2)
        add_to_history(history2, r2, r1)
        result: tuple[int, int] = handle_scoring(r1, r2, wins)
        score = score[0] + result[0], score[1] + result[1]
        i += 1
    return score, wins


def fight_all_bots(bots: dict[str, Bot], n: int = 50) -> Results:
    names = list(bots.keys())
    results = {}
    sleep(0.3)
    print()
    max_num = len(str(len(names) * len(names) // 2))
    battles = 1
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names)):
            b1, b2 = names[i], names[j]
            print(f"Fight {str(battles).rjust(max_num)}: {b1} VS {b2}", end=": ")
            battles += 1
            r, w = fight_bots(bots[b1], bots[b2], n)
            if b1 not in results:
                results[b1] = [0, 0]
            if b2 not in results:
                results[b2] = [0, 0]
            if r[0] is None or r[1] is None:
                if r[0] is None and r[1] is None:
                    print("Failed by Both")
                else:
                    print("Failed by '", end="")
                    if r[0] is None:
                        print(b1 + "'")
                    if r[1] is None:
                        print(b2 + "'")
            else:
                sign = "=" if r[0] == r[1] else (">" if r[0] > r[1] else "<")
                print(r[0], sign, r[1], "|", w[0], ":", w[1])
                results[b1][0] += r[0]
                results[b1][1] += w[0]
                results[b2][0] += r[1]
                results[b2][1] += w[1]
    print()
    return results


def normalise_results(results: Results) -> Results:
    total = sum(v[0] for v in results.values())
    for k in results.copy():
        results[k][0] = results[k][0] / total
    return results


def sort_results(results: Results, normalise: bool) -> list[str]:
    if normalise:
        results = normalise_results(results)
    result = list(results.keys())
    result.sort(key=lambda s: results[s][0], reverse=True)
    out = []
    for r in result:
        if normalise:
            out.append(f"{r}: {results[r][0]:.3f}")
        else:
            out.append(f"{r}: {results[r][0]:,} | {results[r][1]}")
    return out


def print_result(results: Results, normalise: bool = False) -> None:
    print("\n".join(sort_results(deepcopy(results), normalise)), "\n")


if __name__ == '__main__':
    bots = get_all_bots()
    results = fight_all_bots(bots, n=100)
    print_result(results, True)
    print_result(results)
    print(results)