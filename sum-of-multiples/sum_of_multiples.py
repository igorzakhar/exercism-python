def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0

    return sum([
        num for num in range(limit)
        if any(not num % mul for mul in multiples)
    ])
