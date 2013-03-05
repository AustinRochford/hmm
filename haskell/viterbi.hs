import HMM

import Data.List
import Numeric.Container

--viterbi algorithm
viterbi :: HMM -> Dist -> [Emission] -> [Int]
viterbi hmm dist (emiss : emissions) = scanr (!!) (maxIndex dist') maxIxs
    where   (dist', maxIxs) = mapAccumL (viterbiStep hmm) (dist `mul` (emissDist hmm emiss)) emissions
    

--would be nice to write without the where clause; but that gets a bit unwieldy, even with &&&
viterbiStep :: HMM -> Dist -> Emission -> (Dist, [Int])
viterbiStep hmm dist emiss = ((emissDist hmm emiss) `vxl` (map (prod @@>) $ zip prodMaxColIxs [0..]), prodMaxColIxs)
    where   prod = (diag dist) <> (transProbs hmm)
            prodMaxColIxs = map maxIndex $ toColumns prod
            vxl :: Vector Double -> [Double] -> Vector Double
            vxl v = (mul v) . fromList
