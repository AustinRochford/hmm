import Data.Packed.Matrix
import Data.Packed.Vector

--HMM types
type Dist = Vector Prob
type Emission = Int
type Prob = Double
type State = Int

data HMM = HMM {transProbs :: Matrix Prob, emitProbs :: Matrix Prob}

--basic utilities
--this isn't the best name to represent it think more about what it represents
emissDist:: HMM -> Emission -> Dist
emissDist hmm emiss = flatten $ subMatrix (0, emiss) (numStates hmm, 1) $ emitProbs hmm

numStates :: HMM -> Int
numStates = rows . transProbs

--examples
wikiFBEmitProbs = (2><2) [0.9, 0.1, 0.2, 0.8]
wikiFBInitProbs = (1><2) [0.5, 0.5]
wikiFBTransProbs = (2><2) [0.7, 0.3, 0.3, 0.7]
wikiFBHMM = HMM wikiFBTransProbs wikiFBEmitProbs
