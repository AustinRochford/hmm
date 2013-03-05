module HMM where
import Data.Packed.Matrix
import Data.Packed.Vector
import Numeric.Container

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

normalize :: Vector Double -> Dist
normalize v = scale (1 / sumElements v) v

numStates :: HMM -> Int
numStates = rows . transProbs

uniform :: Int -> Dist
uniform n = normalize . (n |>) $ repeat 1

--examples
--forward-backward algorithm
wikiFBEmissions = [0, 0, 1, 0, 0] :: [Emission]
wikiFBEmitProbs = (2><2) [0.9, 0.1, 0.2, 0.8]
wikiFBInitProbs = 2 |> [0.5, 0.5] :: Dist
wikiFBTransProbs = (2><2) [0.7, 0.3, 0.3, 0.7]
wikiFBHMM = HMM wikiFBTransProbs wikiFBEmitProbs

--viterbi algorithm
wikiVitEmissions = [2, 1, 0] :: [Emission] --0=dizzy, 1=cold, 2=normal
wikiVitEmitProbs = (2><3) [0.1, 0.4, 0.5, 0.6, 0.3, 0.1]
wikiVitInitProbs = 2 |> [0.6, 0.4] :: Dist
wikiVitTransProbs = (2><2) [0.7, 0.4, 0.3, 0.6] --0=healthy, 1=fever
wikiVitHMM = HMM wikiVitTransProbs wikiVitEmitProbs
