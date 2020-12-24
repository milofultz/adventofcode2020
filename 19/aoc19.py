P_IN = "aoc19-data"
P_INS = "aoc19-data-small"
P_IN2 = "aoc19-data-p2"
P_IN2S = "aoc19-data-p2-small"


def parse_data(fp) -> (dict, list):
    with open(fp, 'r') as f:
        raw_rules, raw_messages = f.read().split('\n\n')
    rules_dict = dict()
    for rule in raw_rules.split('\n'):
        rule_number, rule_groups = rule.split(": ")
        rules_dict[rule_number] = [group.replace("\"", "").split(' ')
                                   for group in rule_groups.split(" | ")]
    return rules_dict, raw_messages.split('\n')


def get_outputs(rule_number: str, rules: dict, cache: dict) -> set:
    if rule_number in cache:
        return cache[rule_number]
    outputs = set()
    for rule_group in rules[rule_number]:
        output = {""}
        for rule in rule_group:
            if rule in ["a", "b"]:
                output = {element + rule for element in output}
            else:
                result = get_outputs(rule, rules, cache)
                temp = set()
                for element in output:
                    for addition in result:
                        temp.add(element + addition)
                output = temp
        outputs.update(output)
    cache[rule_number] = outputs
    return outputs


def number_of_valid_messages(messages, valid):
    total = 0
    for message in messages:
        total += 1 if message in valid else 0
    return total


if __name__ == "__main__":
    # Part 1
    rules, messages = parse_data(P_IN)
    valid = get_outputs("0", rules, dict())
    print(number_of_valid_messages(messages, valid))
