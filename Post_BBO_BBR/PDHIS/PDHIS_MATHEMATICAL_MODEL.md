# PDHIS mathematical model

## Purpose

Pisharam Delta Hierarchy and Influence State (PDHIS) is a novel mathematical framework for revealing how change takes form within an observed sequence when its generating equation is unknown. It combines a recursive hierarchy of Delta orders with oscillation energy, frequency, temporal dispersion, persistence, cross-order coherence and event-locked examination. It separates established retrospective identification from the next research stage of prospective prediction.

## Observed sequence

For one function, let the ordered output be:

\[
y_1,y_2,\ldots,y_T
\]

The first-order Delta at time \(t\) is:

\[
\Delta^1 y_t=y_t-y_{t-1}
\]

Higher orders are recursive:

\[
\Delta^k y_t=\Delta^{k-1}y_t-\Delta^{k-1}y_{t-1}
\]

Equivalently:

\[
\Delta^k y_t=\sum_{j=0}^{k}(-1)^j {k \choose j}y_{t-j}
\]

This form makes the evidence boundary explicit. Delta order \(k\) requires \(k+1\) observations and first exists at time \(k+1\).

## Scale

Functions with different output ranges are compared using a scale calculated within the available history:

\[
d^k_t=\frac{\Delta^k y_t}{s_{k,t}}
\]

where \(s_{k,t}\) is a non-zero historical scale, such as the standard deviation or robust median absolute movement available by time \(t\). Prospective calculations must not use later observations to define this scale.

## Oscillation

A sign reversal at order \(k\) is:

\[
O^k_t=\mathbf{1}\left(d^k_t d^k_{t-1}<0\right)
\]

The sign-change frequency within a window of length \(w\) is:

\[
\nu^k_t=\frac{1}{w-1}\sum_{r=t-w+2}^{t}O^k_r
\]

With thirteen weekly observations, this sign-change measure is more defensible than a conventional frequency spectrum.

## Energy and temporal dispersion

Oscillation energy within the window is:

\[
E^k_t=\frac{1}{w}\sum_{r=t-w+1}^{t}\left(d^k_r\right)^2
\]

Let the energy-weighted temporal centre be:

\[
\mu^k_t=\frac{\sum_r r\left(d^k_r\right)^2}{\sum_r\left(d^k_r\right)^2}
\]

Temporal dispersion is:

\[
D^k_t=\sqrt{\frac{\sum_r(r-\mu^k_t)^2\left(d^k_r\right)^2}{\sum_r\left(d^k_r\right)^2}}
\]

Energy measures strength. Dispersion measures whether that energy is concentrated or distributed through the pre-event period.

## Persistence and cross-order coherence

Directional persistence is the longest same-sign run divided by the available window length:

\[
R^k_t=\frac{\text{longest same-sign run in }d^k}{w}
\]

Cross-order coherence over orders 1 to \(K\) is:

\[
C_t=\frac{1}{K-1}\sum_{k=1}^{K-1}\mathbf{1}\left(\operatorname{sign}(d^k_t)=\operatorname{sign}(d^{k+1}_t)\right)
\]

Because recursive differencing can create alternating signs mechanically, coherence must always be compared with the binomial pattern expected from repeated differencing alone.

## Signature of Change

The PDHIS descriptive state at time \(t\) is the vector:

\[
S_t=\left[d^1_t,\ldots,d^K_t,\nu_t,E_t,D_t,R_t,C_t\right]
\]

This vector describes direct movement, acceleration, higher-order change, oscillation, energy, temporal spread, persistence and agreement across levels. It is the mathematical Signature of Change.

## Event-locked flicker fingerprint

For a known event at time \(e\), the retrospective fingerprint uses only the preceding window:

\[
F_e=g\left(y_{e-w},\ldots,y_{e-1}\right)
\]

The function \(g\) returns amplitude, energy, dispersion, sign-change frequency, peak spacing, persistence, amplification, Delta 2 energy and flicker density. The event value \(y_e\) does not enter the fingerprint.

## Prospective target

A future event at horizon \(h\) can be defined as:

\[
Y_{t+h}=\mathbf{1}\left(y_{t+h}-y_{t+h-1}>\tau_t\right)
\]

where \(\tau_t\) is fixed from information available by time \(t\). A candidate prediction model is:

\[
P(Y_{t+h}=1\mid S_t)=\frac{1}{1+\exp\left[-(\beta_0+\beta^\top S_t)\right]}
\]

Gradient descent estimates the coefficients. It does not provide separate scientific evidence.

## Evidence rule

PDHIS supports three different levels of conclusion:

1. **Description:** the Delta hierarchy characterises mathematical behaviour already present in the observed sequence.
2. **Retrospective association:** an event-locked fingerprint differs between known event and non-event windows.
3. **Prospective prediction:** a locked signature predicts untouched later outcomes and improves on a simple baseline in discrimination and calibration.

The current BBO record supports detailed description. Matched controls, threshold sensitivity and held-out-function testing locate the present evidence boundary before an advance-warning fingerprint can be locked. PDHIS therefore extracts substantial retrospective mathematical behaviour and defines reliable prospective prediction as the next validation objective.
