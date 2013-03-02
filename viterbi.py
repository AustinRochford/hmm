from hmm import HMM

#the viterbi algorithm
def viterbi(hmm, initial_dist, emissions):
    #it would be nice not to have to treat the initial emission differently, is it possible?
    ix_stack = []
    last_probs = hmm.emission_dist(emissions[0]) * initial_dist

    for emission in emissions[1:]:
        probs = hmm.transition_probs() * last_probs
        max_ixs = np.argmax(last_probs, axis=0)
        ix_stack.append(max_ixs)

        last_probs = hmm.emission_prob(emission) * probs[max_ixs, np.arange(hmm.num_states())]

    states = [np.argmax(last_probs)]

    while ix_stack:
        max_ixs = ix_stack.pop()
        states.append(max_ixs[states[-1]])

    states.reverse()

    return states
