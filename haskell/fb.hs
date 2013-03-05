import HMM

import Numeric.Container

forwardStep :: HMM -> Dist -> Emission -> Dist
forwardStep hmm dist emiss = normalize $ dist <> (transProbs hmm) <> (diag $ emissDist hmm emiss)
