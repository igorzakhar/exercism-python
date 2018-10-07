def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0

    return sum([
        num for num in range(multiples[0], limit)
        if is_multiple(num, multiples)
    ])


def is_multiple(num, multiples):
    for mul in multiples:
        if not num % mul:
            return True
    return False
