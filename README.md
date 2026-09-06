README.md

# Legal Clause Risk Classifier Benchmark

## Project Overview

## Objective

## Risk Categories

## Benchmark Methodology

## Evaluation Metrics

## Repository Structure

## Installation

## Configuration

## Running the Benchmark

## Calculating Metrics

## Benchmark Results

## Error Analysis

## Business Recommendation

## Disclaimer

## Objective

The objective is to determine whether Few-Shot prompting provides a meaningful improvement in legal clause risk classification compared with Zero-Shot prompting, and whether the additional token usage and latency are justified by the improvement in risk detection.

## Risk Categories

| Category | Description |
|---|---|
| High Risk | Significant legal or financial exposure, such as uncapped liability, broad indemnification, or unrestricted termination rights. |
| Medium Risk | Ambiguous, discretionary, or potentially unfavorable commercial terms. |
| Standard / Low Risk | Balanced and clearly defined commercial terms without unusual legal or financial exposure. |

## Benchmark Methodology

## Evaluation Metrics

## Evaluation Metrics

The following metrics are used to compare the two approaches:

- Accuracy
- Macro Precision
- Macro Recall
- Macro F1
- Confusion Matrix
- Average token usage
- Average latency

## Repository Structure
## Repository Structure

```text
legal-clause-risk-classifier-benchmark/
│
├── test_clauses.json
├── prompts.py
├── benchmark_runner.py
├── metrics.py
├── audit_report.md
└── requirements.txt

