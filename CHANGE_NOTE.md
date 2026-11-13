# Revision in response to the checkpoint question

The pasted review asks when the exact guarantee should change a solver choice on a particular checkpoint. The main paper now ends with a concrete choice under the single-output contract. For exact posteriors, the sign test gives a design constraint across priors and scales. For a particular approximate map, the supplement's global Lipschitz-error condition describes when injectivity transfers. Otherwise, recovery, reference fidelity and work on paired calibration states inform the checkpoint choice.

The FFHQ64 example uses two illustrative **mean** forward RMS ceilings against Heun128. Among maps that recovered all 64 clean sources at AA160, Heun2 qualifies at 0.03. At 0.05 both Heun2 and DPM++2S qualify, and DPM++2S uses fewer forward and inverse calls. These are examples of applying a tolerance to the existing panel.

The detailed weight sweep moved out of the main paper and into Supplement G, with every weight, interval and outcome. The main results keep the fact that the successful Heun2 schedule falls outside the universal guarantee. Its exact ratios remain in Supplement B. The split keeps the measured trade-off prominent and gives the reviewer the material qualifications.

The edit uses the pasted review excerpt, the released supplement and the round-two records. It adds no measurements. The release manifest binds the existing code and evidence archives by hash.
