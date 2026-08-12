def average_scores(scores: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    for name, values in scores.items():
        total = 0
        for v in values:
            total += v
        averages[name] = total / len(values)
    return averages


def main() -> None:
    data = {
        "ada": [92, 85, 78],
        "grace": [88, 91],
        "alan": [70, 82, 95, 60],
    }
    result = average_scores(data)
    print(result)


if __name__ == "__main__":
    main()
