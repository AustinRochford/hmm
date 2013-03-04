import Data.Packed.Matrix
import Data.Packed.Vector (Vector)

--HMM types
type Dist = Vector Prob
type Emission = Int
type Prob = Double
type State = Int

data HMM = HMM {transProbs :: Matrix Prob, emitProbs :: Matrix Prob}

--basic utilities
emissDist :: HMM -> Emission -> Dist
emissDist hmm emiss = flatten $ subMatrix (0, emiss) (numStates hmm, 1) $ emitProbs hmm

numStates :: HMM -> Int
numStates = rows . transProbs
