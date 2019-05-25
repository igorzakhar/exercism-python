def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strand_a and strand_b are not equal")
    return len(
        [nucl1 for nucl1, nucl2 in zip(strand_a, strand_b) if nucl1 != nucl2]
    )
