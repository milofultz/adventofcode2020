import copy


P_IN = "aoc19-data"
P_INS = "aoc19-data-small"


def parse_data(fp) -> (dict, list):
    with open(fp, 'r') as f:
        raw_rules, raw_messages = f.read().split('\n\n')
    rules_dict = dict()
    for rule in raw_rules.split('\n'):
        order, nums = rule.split(": ")
        rules_dict[order] = [group.replace("\"", "").split(' ')
                             for group in nums.split(" | ")]
    return rules_dict, raw_messages.split('\n')


def get_outputs(rule_number: str, rules: dict) -> set:
    # * create valid set
    outputs = set()
    # * for rule group in group
    for rule_group in rules[rule_number]:
        # * create output array with empty string inside
        output = [""]
        # * for rule in rule group
        for rule in rule_group:
            # * if rule is "a" or "b"
            if rule in ["a", "b"]:
                # * make output array = element + ("a" or "b") for each element in output
                output = [element + rule for element in output]
            # * else
            else:
                # * set result to func(rules[rule])
                result = get_outputs(rule, rules)
                # * create temporary array
                temp = list()
                # * for element in output array
                for element in output:
                    # * for addition in result
                    for addition in result:
                        # * add element + addition to temporary array
                        temp.append(element + addition)
                output = copy.deepcopy(temp)
        # * add all of output array to valid set
        outputs.update(output)
    # * return valid set
    return outputs


if __name__ == "__main__":
    rules, messages = parse_data(P_INS)
    valid = get_outputs("0", rules)
