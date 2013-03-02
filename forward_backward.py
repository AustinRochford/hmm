from hmm import HMM
import numpy as np

#forward-backward algorithm
def backward(hmm, emissions):
    dist = uniform(hmm.num_states)
    dists = [dist]

    for emission in reversed(emissions):
        dist = normalize(np.dot(hmm.transition_probs, np.dot(np.diagflat(hmm.emission_dist(emission)), dist.T)).T)
        dists.insert(0, dist)

    return np.squeeze(np.array(dists))

def forward_backward(hmm, initial_dist, emissions):
    forward_dists = forward(hmm, initial_dist, emissions)
    backward_dists = backward(hmm, emissions)

    #also, this is a bit of a monster of a line of code
    return np.multiply(forward_dists, backward_dists) / np.reshape(np.sum(np.multiply(forward_dists, backward_dists), axis=1), (len(emissions) + 1, 1))

def forward(hmm, initial_dist, emissions):
    dist = initial_dist
    dists = [dist]

    for emission in emissions:
        dist = normalize(np.dot(dist, np.dot(hmm.transition_probs, np.diagflat(hmm.emission_dist(emission)))))
        dists.append(dist)

    return np.squeeze(np.array(dists))

#related utilities
def emission_dist(emission_probs, emission):
    return np.diagflat(emission_probs[:, emission])

def normalize(array_):
    #very tightly coupled to the way we expect distributions to be stored
    return array_ / np.sum(array_, axis=1)

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
    #print(forward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_emissions))
    #print(backward(wiki_transition_probs, wiki_emission_probs, wiki_emissions))
    print(forward_backward(wiki_HMM, wiki_initial_dist, wiki_emissions))
