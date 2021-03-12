# Luo-Rudy1_SIADS2020
This repository contains AUTO scripts and some printouts for the analysis presented in the SIAM Journal on Applied Dynamical Sysytems (2020) article:
"Big Ducks in the Heart: Canard Analysis Can Explain Large Early Afterdepolarizations in Cardiomyocytes"

- Archive_EAD_DesingLuo_dinf contains AUTO scripts for a bifurcation analysis of the desingularized reduced system as well as the .xml vector field file used to generate the AUTO C file and the .ode file
- Archive_EAD_Luo contains contains AUTO scripts for a bifurcation analysis of the full (modified, see manuscript) system
- canard0 and canard1 contain the AUTO scripts used to compute the primary strong canard (canard0, &gamma;<sub>0</sub>) and the first secondary maximal canard (canard1, &gamma;<sub>1</sub>)

Abstract:
Early afterdepolarizations (EADs) are pathological voltage fluctuations that can occur in cardiac cells
and are a potent source of potentially fatal arrhythmias. Recent works examining the mechanisms
underlying EADs in minimal computational cardiac models have revealed that voltage-driven EADs
are canard-induced mixed-mode oscillations whose properties are mediated by the rate at which
these cells are paced. In this work, we analyze the mechanisms for the pacing-induced generation of
different EAD behaviors in a reduced four-dimensional Luo-Rudy I model using slow-fast analysis.
While previous explanations for EADs in this model have required manipulation of the underlying
multitimescale structure, our approach does not and we find that the canard mechanism persists in
generating EADs in this context. We also find that the canard mechanism gives a more complete
explanation for the onset and properties of the EADs induced (e.g., EAD amplitude and number). In
addition, we also find that the canards play an essential role in producing a richer set of behaviors than
were seen in other minimal models, some of which have also been observed in experiments. These
behaviors include pacing-induced termination of EADs, the periodic alternation of cardiac action
potentials with and without EADs, as well as bistability between standard and EAD-containing
action potentials at a fixed pacing rate. Finally, we show that this bistability can lead to hysteretic
transitions between standard and arrhythmogenic action potentials under sufficiently slow oscillations
in the pacing rate.

Read More: https://epubs.siam.org/doi/abs/10.1137/19M1300777
