from numpy import diagflat

#forward-backward algorithm
def forward(transition_probs, emission_probs, initial_dist, emissions):
    dists = [init]
    dist = init

    for emission in emissions:
        dists.append(dot(dist, dot(transition_probs, emission_marix(emission_probs, emissions))))

    return dists

#distribution manipulation utilities
def emission_matrix(emission_probs, emission):
    return diagflat(emission_probs[:, emission])

def to_dist(v):
    return (1 / sum(abs(v.flatten()))) * v
