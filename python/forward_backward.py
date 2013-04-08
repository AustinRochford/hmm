from hmm import HMM
import numpy as np

#forward-backward algorithm
def backward(hmm, emissions):
    dist = uniform(hmm.num_states)
    dists = [dist]

    for emission in reversed(emissions):
        dist = backward_step(hmm, dist, emission)
        dists.append(dist)

    dists.reverse()

    return np.row_stack(dists)

def backward_step(hmm, dist, emission):
    return normalize(np.dot(hmm.transition_probs, np.dot(np.diagflat(hmm.emission_dist(emission)), dist.T)).T)

def forward_backward(hmm, initial_dist, emissions):
    forward_dists = forward(hmm, initial_dist, emissions)
    backward_dists = backward(hmm, emissions)

    return normalize(np.multiply(forward_dists, backward_dists))

def forward(hmm, initial_dist, emissions):
    dist = initial_dist
    dists = [dist]

    for emission in emissions:
        dist = forward_step(hmm, dist, emission)
        dists.append(dist)

    return np.row_stack(dists)

def forward_step(hmm, dist, emission):
    return normalize(np.dot(dist, np.dot(hmm.transition_probs, np.diagflat(hmm.emission_dist(emission)))))

#related utilities
def modify_tuple(tuple_, ix, value):
    as_list = list(tuple_)
    as_list[ix] = value

    return tuple(as_list)

def normalize(array, axis=1):
    sum_shape = modify_tuple(array.shape, axis, 1)
    return array / np.reshape(np.sum(array, axis=axis), sum_shape)

def uniform(n):
    return normalize(np.ones((1,n)))

#examples
#from wikipedia
wiki_emission_probs = np.array([[0.9, 0.1], [0.2, 0.8]])
wiki_initial_dist = np.array([[0.5, 0.5]])
wiki_emissions = [0, 0, 1, 0, 0]
wiki_transition_probs = np.array([[0.7, 0.3], [0.3, 0.7]])
wiki_HMM = HMM(wiki_transition_probs, wiki_emission_probs)

if __name__ == "__main__":
    #print(forward(wiki_HMM, wiki_initial_dist, wiki_emissions))
    #print(backward(wiki_HMM, wiki_emissions))
    print(forward_backward(wiki_HMM, wiki_initial_dist, wiki_emissions))
