from hmm import HMM

def viterbi(hmm, initial_dist, emissions):
    #it would be nice not to have to treat the initial emission differently
    ix_stack = []
    last_probs = hmm.emission_dist(emissions[0]) * initial_dist
    prob_stack = [last_probs]

    for emission in emissions[1:]:
        max_ixs = np.argmax(hmm.transition_probs() * last_probs,
