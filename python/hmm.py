class HMM:
    #constructor
    #transition_probs[i, j] is the probability of transitioning to state i from state j
    #emission_probs[i, j] is the probability of emitting emission j while in state i
    def __init__(self, transition_probs, emission_probs):
        self._transition_probs = transition_probs
        self._emission_probs = emission_probs

    #accessors
    def emission_dist(self, emission):
        return self._emission_probs[:, emission]

    @property
    def num_states(self):
        return self._transition_probs.shape[0]

    @property
    def transition_probs(self):
        return self._transition_probs
