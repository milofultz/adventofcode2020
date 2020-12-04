from aoc03 import main as get_trees_encountered


def main():
    answers = 1
    for i in range(5):
        answers *= get_trees_encountered()
    print(answers)


if __name__ == '__main__':
    main()
