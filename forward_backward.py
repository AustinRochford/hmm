import numpy as np

#forward-backward algorithm
def forward(transition_probs, emission_probs, initial_dist, emissions):
    dist = initial_dist
    dists = [dist]

    for emission in emissions:
        dist = normalize(np.dot(dist, np.dot(transition_probs, emission_dist(emission_probs, emission))))

#related utilities
def emission_dist(emission_probs, emission):
    return np.diagflat(emission_probs[emission, :])

def l1norm(array_):
    return np.linalg.norm(array_, np.inf)

def normalize(array_):
    return array_ / l1norm(array_)

#examples
#from wikipedia
wiki_emission_probs = np.array([[0.9, 0.1], [0.2, 0.8]])
wiki_initial_dist = np.array([[0.5, 0.5]])
wiki_emissions = [0, 0, 1, 0, 0]
wiki_transition_probs = np.array([[0.7, 0.3], [0.3, 0.7]])

if __name__ == "__main__":
    #print(forward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_emissions))
    #print(backward(wiki_transition_probs, wiki_emission_probs, wiki_emissions))
    #print(forward_backward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_emissions))
    print(emission_dist(wiki_emission_probs, 0))
