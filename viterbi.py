from hmm import HMM
import numpy as np

#the Viterbi algorithm
def viterbi(hmm, initial_dist, emissions):
    pass

#examples
#from Wikipedia
wiki_transition_probs = np.array([[0.7, 0.4], [0.3, 0.6]]) #0=Healthy, 1=Fever
wiki_emissions = [2, 1, 0]
wiki_emission_probs = np.array([[0.1, 0.6], [0.4, 0.3], [0.5, 0.1]]).T #0=Dizzy, 1=Cold, 2=Normal
wiki_initial_dist = np.array([[0.6, 0.4]])
wiki_hmm = HMM(wiki_transition_probs, wiki_emission_probs)

if __name__ == "__main__":
    print(viterbi(wiki_hmm, wiki_initial_dist, wiki_emissions))
