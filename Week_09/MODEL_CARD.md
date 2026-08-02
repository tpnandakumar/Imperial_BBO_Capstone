# Week 09 Model Card

## Identification

- Course module: 21
- Capstone week: 09
- Optimisation round: 9
- System: Human supervised, LLM assisted black box optimisation workflow
- Maintainer: Dr N T Pisharam

## Model information

### Description

The Week 09 optimisation system combines historical query and output data, structured analysis, human judgement and model assisted reasoning to recommend one new query vector for each of eight hidden objective functions.

### Purpose

The system is designed to improve objective values under a limited query budget while preserving enough exploration to reduce uncertainty and avoid premature convergence.

### Architecture

The workflow contains five stages:

1. retrieve prior inputs and outputs;
2. compare recent and historical performance;
3. classify each function as exploit, refine, explore or reassess;
4. generate candidate query vectors;
5. apply human review before submission.

### Inputs

- historical query vectors;
- historical objective values;
- function dimensionality and domain constraints;
- recent performance changes;
- qualitative confidence and uncertainty judgements.

### Outputs

- one six-decimal query vector for each function;
- a transparent strategy label for each function;
- rationale, expected benefit and risk for the selected query.

## Week 09 strategy profile

| Function | Week 09 output | Strategy |
|---|---:|---|
| F1 | -1.4546199699251391e-58 | Explore |
| F2 | 0.47297842839949866 | Refine |
| F3 | -0.1156707106126581 | Reassess |
| F4 | -11.788939969158545 | Refine |
| F5 | 4394.868042481448 | Exploit |
| F6 | -1.1733030029888645 | Reassess |
| F7 | 1.314307996450604 | Refine |
| F8 | 9.4709436 | Refine |

## Evaluation approach

Evaluation uses observed black box outputs rather than access to the true functions. The principal checks are:

- change from the preceding round;
- best-so-far progression;
- stability across neighbouring queries;
- rank across functions, interpreted cautiously because scales differ;
- consistency between evidence, confidence and selected strategy;
- compliance with input bounds and dimensionality.

## Performance interpretation

Function 5 remained the dominant positive performer and improved from Week 08 to Week 09. Function 4 moved towards a less negative value. Functions 2, 3, 6, 7 and 8 declined by varying amounts, while Function 1 remained effectively unchanged near zero. These results justified differentiated rather than uniform query selection.

## Intended use

- weekly BBO query recommendation;
- transparent explanation of query selection;
- comparison of strategy evolution across rounds;
- educational analysis of black box optimisation under uncertainty.

## Out of scope

- autonomous unsupervised submission;
- proof of global optimality;
- inference of hidden analytical functions;
- transfer to unrelated optimisation tasks without validation;
- safety critical or clinical decision making.

## Known limitations

- very small sequential dataset;
- unknown objective functions and noise properties;
- heterogeneous output scales;
- adaptive sampling bias;
- potential overfitting to recent observations;
- qualitative confidence estimates;
- dependence on human judgement.

## Risk controls

- mandatory human review;
- exact dimensionality and range checks;
- comparison with prior submissions;
- preservation of exploratory capacity;
- explicit assumptions and alternatives;
- reproducible code and retained raw data.

## Transparency links

- Data files and schemas: [DATASET.md](DATASET.md)
- Data provenance and limitations: [DATASHEET.md](DATASHEET.md)
- Query rationale: [DECISION_CARD.md](DECISION_CARD.md)
- Validation: [VALIDATION.md](VALIDATION.md)
- Assumptions: [ASSUMPTIONS.md](ASSUMPTIONS.md)
- Weekly changes: [CHANGELOG.md](CHANGELOG.md)
