P_IN = "aoc19-data"
P_INS = "aoc19-data-small"


def parse_data(fp) -> (dict, list):
    with open(fp, 'r') as f:
        raw_rules, raw_messages = f.read().split('\n\n')
    rules_dict = dict()
    for rule in raw_rules.split('\n'):
        order, nums = rule.split(": ")
        rules_dict[order] = [group.replace("\"", "")
                             for group in nums.split(" | ")]
    return rules_dict, raw_messages.split('\n')


if __name__ == "__main__":
    rules, messages = parse_data(P_INS)
    print(rules, messages)
