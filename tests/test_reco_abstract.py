import idresearch

url = 'https://arxiv.org/abs/2106.10353'
i = 59               # User will choose this corresponding to the citation count which he wants to refer in the actual program
abs = idresearch.reco_abstract(i,url)
test_abs = "The μνSSM is a simple supersymmetric extension of the Standard Model (SM) capable of predicting neutrino physics in agreement with experiment. In this paper we perform the complete one-loop renormalization of the neutral scalar sector of the μνSSM with one generation of right-handed neutrinos in a mixed on-shell/DR scheme. The renormalization procedure is discussed in detail, emphasizing conceptual differences to the minimal (MSSM) and next-to-minimal (NMSSM) supersymmetric standard model regarding the field renormalization and the treatment of nonflavor-diagonal soft mass parameters, which have their origin in the breaking of R-parity in the μνSSM. We calculate the full one-loop corrections to the neutral scalar masses of the μνSSM. The one-loop contributions are supplemented by available MSSM higher-order corrections. We obtain numerical results for a SM-like Higgs boson mass consistent with experimental bounds. We compare our results to predictions in the NMSSM to obtain a measure for the significance of genuine μνSSM-like contributions. We only find minor corrections due to the smallness of the neutrino Yukawa couplings, indicating that the Higgs boson mass calculations in the μνSSM are at the same level of accuracy as in the NMSSM. Finally we show that the μνSSM can accomodate a Higgs boson that could explain an excess of γ γ events at ∼ 96 GeV as reported by CMS, as well as the 2 σ excess of bb̄ events observed at LEP at a similar mass scale."

if abs == test_abs:
    print("Test Passed")
else:
    print("Test Failed")

