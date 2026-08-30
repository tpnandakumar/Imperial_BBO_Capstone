# PDHIS mathematical model

## Purpose

Pisharam Delta Hierarchy and Influence State (PDHIS) is a novel integrated framework for examining how behavioural change takes form within an observed sequence when its generating equation is unknown. It combines recursive Delta structure, oscillation energy, temporal dispersion, persistence, cross-order coherence and event-locked analysis into a single mathematical Signature of Change.

PDHIS distinguishes three questions. What mathematical behaviour is already present in the record? Did a known event have a detectable earlier flicker? Can a signature fixed in advance predict a later event? The thirteen-week Black Box Optimisation (BBO) record supports detailed description and retrospective investigation. Prospective prediction remains a separate validation stage.

## Notation and evidence boundary

For one function, let the ordered output sequence be:

$$
y_1,y_2,\ldots,y_T
$$

Here, $t$ is time, $T$ is the number of observations, $k$ is the Delta order, $K$ is the highest order examined and $w$ is the number of valid values in a local window.

A Delta of order $k$ first exists at $t=k+1$. Its valid range and number of values are:

$$
t=k+1,\ldots,T
$$

$$
N_k=T-k
$$

For the eight functions in the Imperial BBO record:

$$
N_k^{\mathrm{all}}=8(T-k)
$$

These are raw descriptive values. An analysis pairing a Delta with a later outcome has fewer usable pairs.

## Recursive Delta hierarchy

The first-order Delta measures movement between consecutive observations:

$$
\Delta^1y_t=y_t-y_{t-1}
$$

Higher orders are calculated recursively:

$$
\Delta^ky_t=\Delta^{k-1}y_t-\Delta^{k-1}y_{t-1}
$$

The equivalent closed form is:

$$
\Delta^ky_t=\sum_{j=0}^{k}(-1)^j\binom{k}{j}y_{t-j}
$$

Delta 1 measures movement. Delta 2 measures change in that movement. Higher orders identify progressively finer changes in local mathematical behaviour. They also amplify small fluctuations, so they must be interpreted with energy, persistence, propagation and a suitable comparison pattern.

### Worked example

Consider:

$$
y_1=10,\qquad y_2=12,\qquad y_3=11,\qquad y_4=15
$$

The first-order Deltas are:

$$
\Delta^1y_2=12-10=2,\qquad
\Delta^1y_3=11-12=-1,\qquad
\Delta^1y_4=15-11=4
$$

The second-order Deltas are:

$$
\Delta^2y_3=(-1)-2=-3,\qquad
\Delta^2y_4=4-(-1)=5
$$

The sequence changes direction at Delta 1. Delta 2 shows that its rate of movement also changes sharply.

## Historical scaling

Functions with different output ranges require a common scale:

$$
d_t^k=\frac{\Delta^ky_t}{s_{k,t}}
$$

A robust historical scale is:

$$
s_{k,t}=\max\left\{1.4826\mathrm{MAD}\left(\Delta^ky_{k+1},\ldots,\Delta^ky_t\right),\varepsilon\right\}
$$

For historical values $x_1,\ldots,x_n$, the median absolute deviation is:

$$
\mathrm{MAD}(x)=\mathop{\mathrm{median}}_i\left|x_i-\mathop{\mathrm{median}}_j(x_j)\right|
$$

The constant 1.4826 makes the measure comparable with the standard deviation under a normal reference distribution. The term $\varepsilon>0$ prevents division by zero. If there are too few values for a reliable scale, the analysis must report the unscaled Delta or use a scale fixed in advance. Prospective calculations may use information available by time $t$, but never later observations.

### Worked example

If $\Delta^1y_t=4$ and $s_{1,t}=2$, then:

$$
d_t^1=\frac{4}{2}=2
$$

The current movement is two historical scale units in magnitude.

## Oscillation and sign-change frequency

Define the sign function as:

$$
\mathrm{sgn}(x)=
\begin{cases}
-1, & x<0\\
0, & x=0\\
1, & x>0
\end{cases}
$$

Zero values are neutral. Within a chosen window, let $z_1^k,\ldots,z_m^k$ be the ordered signs after zero values have been removed:

$$
z_q^k\in\{-1,1\},\qquad q=1,\ldots,m
$$

A sign reversal is:

$$
O_q^k=\mathbf{1}\left(z_q^kz_{q-1}^k<0\right),\qquad q=2,\ldots,m
$$

For a window containing $m$ valid non-zero Delta values, sign-change frequency is:

$$
\nu_t^k=\frac{1}{m-1}\sum_{q=2}^{m}O_q^k
$$

The value lies between 0 and 1. Zero means no adjacent signs reverse. One means every adjacent pair reverses. With thirteen weekly observations, this is more defensible than estimating a conventional frequency spectrum.

### Worked example

For the scaled values:

$$
0.5,\ -0.4,\ 0.6,\ -0.3
$$

all three adjacent pairs reverse sign:

$$
\nu_t^k=\frac{3}{4-1}=1
$$

This window contains continuous alternation. It does not, by itself, prove that an event will follow.

## Oscillation energy

Oscillation energy is the mean squared magnitude of the scaled Delta values:

$$
E_t^k=\frac{1}{w}\sum_{r=t-w+1}^{t}\left(d_r^k\right)^2
$$

Energy is non-negative. A larger value indicates stronger scaled movement, but not necessarily more frequent sign changes.

### Worked example

Using the same four values:

$$
E_t^k=\frac{0.5^2+(-0.4)^2+0.6^2+(-0.3)^2}{4}
$$

$$
E_t^k=\frac{0.25+0.16+0.36+0.09}{4}=0.215
$$

The window has a mean squared scaled magnitude of 0.215.

## Energy-weighted temporal centre and dispersion

The energy-weighted temporal centre is:

$$
\mu_t^k=
\frac{\displaystyle\sum_{r=t-w+1}^{t}r\left(d_r^k\right)^2}
{\displaystyle\sum_{r=t-w+1}^{t}\left(d_r^k\right)^2}
$$

Temporal dispersion is:

$$
D_t^k=
\sqrt{
\frac{\displaystyle\sum_{r=t-w+1}^{t}\left(r-\mu_t^k\right)^2\left(d_r^k\right)^2}
{\displaystyle\sum_{r=t-w+1}^{t}\left(d_r^k\right)^2}
}
$$

If the denominator is zero, both measures are undefined because the window contains no Delta energy. The temporal centre shows where energy is concentrated. Dispersion shows whether it is localised or distributed across the window.

### Worked example

At relative positions $r=1,2,3,4$, the squared weights are $0.25,0.16,0.36,0.09$. Therefore:

$$
\mu_t^k=\frac{1(0.25)+2(0.16)+3(0.36)+4(0.09)}{0.86}=2.34
$$

Substitution into the dispersion equation gives:

$$
D_t^k\approx1.01
$$

The energy is centred slightly before the middle and is spread across about one observation on either side.

## Directional persistence

Let $n_{k,t}$ be the number of valid non-zero values in the window. Directional persistence is:

$$
R_t^k=
\frac{\text{longest same-sign run among the valid }d_r^k\text{ values}}
{n_{k,t}}
$$

A value near 1 indicates sustained direction. A smaller value indicates frequent reversal.

### Worked example

For the sign sequence:

$$
+,+,+,-,-,+
$$

the longest same-sign run has length 3:

$$
R_t^k=\frac{3}{6}=0.5
$$

## Cross-order coherence

Cross-order coherence measures directional agreement between adjacent Delta orders. It is available only when $t\geq K+1$. Let $V_t$ be the set of adjacent-order pairs for which both values are non-zero:

$$
V_t=\left\{k\in\{1,\ldots,K-1\}:d_t^k\ne0\text{ and }d_t^{k+1}\ne0\right\}
$$

Then:

$$
C_t=
\frac{1}{|V_t|}
\sum_{k\in V_t}
\mathbf{1}\left[
\mathrm{sgn}\left(d_t^k\right)
=
\mathrm{sgn}\left(d_t^{k+1}\right)
\right]
$$

If $V_t$ is empty, coherence is undefined. Repeated differencing can create alternating signs mechanically. Observed coherence must therefore be compared with reference sequences, such as shuffled increments or simulated noise with matched variance.

### Worked example

If four Delta orders have signs:

$$
+,+,-,-
$$

two of the three adjacent-order pairs agree:

$$
C_t=\frac{2}{3}=0.667
$$

## Mathematical Signature of Change

Define the component vectors:

$$
\mathbf{d}_t=\left(d_t^1,\ldots,d_t^K\right)
$$

$$
\boldsymbol{\nu}_t=\left(\nu_t^1,\ldots,\nu_t^K\right),\qquad
\mathbf{E}_t=\left(E_t^1,\ldots,E_t^K\right)
$$

$$
\mathbf{D}_t=\left(D_t^1,\ldots,D_t^K\right),\qquad
\mathbf{R}_t=\left(R_t^1,\ldots,R_t^K\right)
$$

The complete PDHIS state is:

$$
S_t=\left[
\mathbf{d}_t,
\boldsymbol{\nu}_t,
\mathbf{E}_t,
\mathbf{D}_t,
\mathbf{R}_t,
C_t
\right]
$$

This state combines movement, acceleration, higher-order variation, oscillation frequency, strength, temporal spread, persistence and agreement across Delta levels. It is the mathematical Signature of Change already present in the observed sequence.

## Event-locked flicker fingerprint

For a known event at time $e$, define a pre-event window that excludes the event value:

$$
W_e=\left(y_{e-w},\ldots,y_{e-1}\right)
$$

Earlier observations may initialise Delta calculations at the left boundary, but do not enter the summarised window. The fingerprint is:

$$
F_e=g(W_e)
$$

A reproducible form is:

$$
F_e=\left[
\mathbf{A}_e,
\mathbf{E}_e,
\mathbf{D}_e,
\boldsymbol{\nu}_e,
\mathbf{R}_e,
\mathbf{G}_e,
\boldsymbol{\phi}_e
\right]
$$

Maximum absolute amplitude at each order is:

$$
A_e^k=\max_{r\in W_e}\left|d_r^k\right|
$$

Let $M_e^k$ be the number of eligible adjacent non-zero sign comparisons in the pre-event window. Flicker density is:

$$
\phi_e^k=
\frac{\displaystyle\sum_{q=2}^{M_e^k+1}O_q^k}
{M_e^k}
$$

If $M_e^k=0$, flicker density is undefined.

To measure build-up, divide the pre-event window into an early half $W_e^{(a)}$ and late half $W_e^{(b)}$. Energy amplification is:

$$
G_e^k=\frac{E_{e,b}^k+\varepsilon}{E_{e,a}^k+\varepsilon}
$$

A value above 1 indicates stronger Delta energy nearer the event. The event value $y_e$ never enters the fingerprint. This prevents the outcome from defining its own proposed precursor.

## Prospective event target

A two-sided behavioural event at future horizon $h$ is:

$$
Y_{t+h}=\mathbf{1}\left(\left|y_{t+h}-y_{t+h-1}\right|>\tau_t\right)
$$

Its direction is recorded separately:

$$
Q_{t+h}=\mathrm{sgn}\left(y_{t+h}-y_{t+h-1}\right)
$$

Here, $\tau_t$ is fixed using information available by time $t$. If the question concerns improvement only, the positive target is:

$$
Y_{t+h}^{+}=\mathbf{1}\left(y_{t+h}-y_{t+h-1}>\tau_t\right)
$$

## Candidate prospective model

A candidate logistic model is:

$$
\Pr\left(Y_{t+h}=1\mid S_t\right)=
\frac{1}{1+\exp\left[-\left(\beta_0+\boldsymbol{\beta}^{\mathsf T}S_t\right)\right]}
$$

For $n$ prospectively eligible observations, the negative log-likelihood is:

$$
\mathcal{L}(\boldsymbol{\beta})=
-\sum_{i=1}^{n}\left[Y_i\log(p_i)+(1-Y_i)\log(1-p_i)\right]
$$

Gradient descent updates the coefficients through:

$$
\boldsymbol{\beta}^{(m+1)}=
\boldsymbol{\beta}^{(m)}-\eta\nabla_{\boldsymbol{\beta}}\mathcal{L}\left(\boldsymbol{\beta}^{(m)}\right)
$$

Here, $\eta>0$ is the learning rate. Gradient descent estimates the model. It does not provide separate evidence that the Signature of Change predicts future behaviour.

## Interpretation rule

A high-order oscillation is not automatically meaningful. Its interpretation becomes stronger when several features occur together:

1. Delta energy rises above its historical reference level.
2. Oscillation persists across more than one observation.
3. The pattern propagates coherently across Delta orders.
4. Temporal dispersion or amplification shows organised development towards an event.
5. The pattern differs from matched non-event windows and reference sequences.
6. The same locked rule performs on untouched later observations.

The Delta hierarchy does not govern the unknown function. It identifies a mathematical Signature of Change expressed by the observed sequence. The governing function remains unknown unless independently recovered and validated.

## Evidence rule

PDHIS supports three levels of conclusion:

1. **Description:** the Delta hierarchy characterises mathematical behaviour already present in the observed sequence.
2. **Retrospective association:** a fingerprint calculated before known events differs from fingerprints calculated before matched non-events.
3. **Prospective prediction:** a rule fixed in advance predicts untouched later outcomes and improves on a simple baseline in both discrimination and calibration.

The present Imperial BBO record supports detailed mathematical description and event-locked retrospective investigation. Matched controls, threshold sensitivity, reference sequences and held-out-function testing define the next evidence boundary. PDHIS therefore extracts substantial retrospective mathematical behaviour while providing a clear and testable route towards prospective prediction.


