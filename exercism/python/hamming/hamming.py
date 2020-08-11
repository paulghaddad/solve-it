def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not the same length.')

    differences = 0

    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            differences += 1

    return differences
