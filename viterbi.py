from hmm import HMM

def viterbi(hmm, initial_dist, emissions):
    #it would be nice not to have to treat the initial emission differently
    ix_stack = []
    prob_stack = [hmm.emission_dist(emissions[0]) * initial_dist]

    for emission in emissions[1:]:
        last_probs = hmm.transition_probs() * prob_stack[-1]
        max_ixs = np.argmax(last_probs, axis=0)
        ix_stack.append(max_ixs)

        prob_stack.append(hmm.emission_dist(emission) * last_probs[max_ixs, np.arange(hmm.num_states())])
