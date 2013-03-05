import HMM

import Data.List
import Numeric.Container

--forward algorithm
forward :: HMM -> Dist -> [Emission] -> [Dist]
forward hmm = scanl (forwardStep hmm)

forwardStep :: HMM -> Dist -> Emission -> Dist
forwardStep hmm dist emiss = normalize $ dist <> (transProbs hmm) <> (diag $ emissDist hmm emiss)
