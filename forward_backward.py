from numpy import diagflat

def emission_matrix(emission_probs, emission):
    return diagflat(emission_probs[:, emission])

def to_dist(v):
    return (1 / sum(abs(v.flatten()))) * v
