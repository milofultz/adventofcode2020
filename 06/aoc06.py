PUZZLE_INPUT = 'aoc06-data'


def get_groups_from_data():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read()
    return data.split('\n\n')


def get_total_answer_count(groups) -> int:
    total = 0
    for group in groups:
        total += len(get_group_answers(group))
    return total


def get_group_answers(group) -> set:
    answers = set()
    for answer in group.replace('\n', ''):
        answers.add(answer)
    return answers


if __name__ == "__main__":
    groups = get_groups_from_data()
    print(get_total_answer_count(groups))
