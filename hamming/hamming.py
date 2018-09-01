def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strand_a and strand_b are not equal")
    return len([nuc for nuc in zip(strand_a, strand_b) if nuc[0] != nuc[1]])
