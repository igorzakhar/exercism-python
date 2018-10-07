def f(stop, args):
    sum = 0
    for i in range(args[0], stop):
        for a in args:
            if not i % a:
                sum += i
    return sum
