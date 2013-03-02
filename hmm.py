import numpy as np

class HMM:
    #constructor
    def __init__(self, transition_probs, emission_probs):
        self._transition_probs = transition_probs
        self._emission_probs = emission_probs

    #accessor
    def emission_dist(emission):
        return self._emission_probs[:, emission]
