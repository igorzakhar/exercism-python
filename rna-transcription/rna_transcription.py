def to_rna(dna_strand):
    replacements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([
        nucl.replace(nucl, replacements[nucl])
        for nucl in dna_strand if nucl in replacements.keys()
    ])
