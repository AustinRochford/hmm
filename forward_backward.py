from numpy import diagflat

#forward-backward algorithm
def forward(transition_probs, emission_probs, initial_dist, emissions):
    dists = [initial_dist]
    dist = initial_dist

    for emission in emissions:
        dists.append(dot(dist, dot(transition_probs, emission_marix(emission_probs, emissions))))

    return dists

#distribution manipulation utilities
def emission_matrix(emission_probs, emission):
    return diagflat(emission_probs[:, emission])

def to_dist(v):
    return (1 / sum(abs(v.flatten()))) * v

#examples
#from wikipedia
wiki_emission_probs = array([[0.9, 0.1], [0.2, 0.8]])
wiki_initial_dist = array([[0.5, 0.5]])
wiki_emissions = [0, 0, 1, 0, 0]
wiki_transition_probs = array([[0.7, 0.3], [0.3, 0.7]])

if __name__ == "__main__":
    print forward(wiki_transition_probs, wiki_emission_probs, wiki_initial_dist, wiki_states)
