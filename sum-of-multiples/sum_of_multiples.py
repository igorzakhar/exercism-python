def sum_of_multiples(limit, multiples):
    return sum([
        num for num in range(limit)
        if any(num % mul == 0 for mul in multiples)
    ])
