from hmm import HMM
import numpy as np

#the Viterbi algorithm
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

#examples
#from Wikipedia
wiki_transition_probs = np.array([[0.7, 0.4], [0.3, 0.6]]) #0=Healthy, 1=Fever
wiki_emissions = [2, 1, 0]
wiki_emission_probs = np.array([[0.1, 0.6], [0.4, 0.3], [0.5, 0.1]])#0=Dizzy, 1=Cold, 2=Normal
wiki_initial_dist = np.array([[0.6, 0.4]])
wiki_hmm = HMM(wiki_transition_probs, wiki_emission_probs)

if __name__ == "__main__":
    print(viterbi(wiki_hmm, wiki_initial_dist, wiki_emissions))
