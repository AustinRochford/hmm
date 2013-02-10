from numpy import array, diagflat, dot, transpose
from operator import mul

#forward-backward algorithm
def backward(transition_probs, emission_probs, emissions):
    dist = to_dist(array([[1.0] * emission_probs.shape[0]]))
    dists = [dist]

    for emission in reversed(emissions):
        dist = transpose(to_dist(dot(transition_probs, dot(emission_matrix(emission_probs, emission), transpose(dist)))))
        dists.append(dist)

    return dists

def forward(transition_probs, emission_probs, initial_dist, emissions):
    dist = initial_dist
    dists = [initial_dist]

    for emission in emissions:
        dist = to_dist(dot(dist, dot(transition_probs, emission_matrix(emission_probs, emission))))
        dists.append(dist)

    return dists

def forward_backward(transition_probs, emission_probs, initial_dist, emissions):
    forward_dists = forward(transition_probs, emission_probs, initial_dist, emissions)
    backward_dists = backward(transition_probs, emission_probs, emissions)
    backward_dists.reverse()

    return [to_dist(mul(*dists)) for dists in zip(forward_dists, backward_dists)]

#distribution manipulation utilities
def emission_matrix(emission_probs, emission):
    return diagflat(emission_probs[:, emission])

def to_dist(v):
    return v / sum(abs(v.flatten()))

#examples
#from wikipedia
wiki_emission_probs = array([[0.9, 0.1], [0.2, 0.8]])
wiki_initial_dist = array([[0.5, 0.5]])
wiki_emissions = [0, 0, 1, 0, 0]
wiki_transition_probs = array([[0.7, 0.3], [0.3, 0.7]])

if __name__ == "__main__":
    #print forward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_emissions)
    #print backward(wiki_transition_probs, wiki_emission_probs, wiki_emissions)
    print forward_backward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_emissions)
