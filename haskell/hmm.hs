import Data.Packed.Matrix (Matrix, rows)
import Data.Packed.Vector (Vector)

--HMM types
type Dist = Vector Prob
data HMM = HMM {transProbs :: Matrix Prob, emitProbs :: Matrix Prob}
type Prob = Double

--basic utilities
numStates :: HMM -> Int
numStates = rows . transProbs
