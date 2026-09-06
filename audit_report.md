# Legal Clause Risk Classifier
# Zero-Shot vs Few-Shot Audit Report

## 1. Objective

This project evaluates Zero-Shot and Few-Shot prompting strategies
for identifying legal and commercial risk in contract clauses.

The three classifications are:

- High Risk
- Medium Risk
- Standard / Low Risk

The objective is to determine whether Few-Shot prompting improves
classification performance compared with Zero-Shot prompting.

---

## 2. Dataset

The benchmark contains 15 contract clauses:

| Category | Number |
|---|---:|
| High Risk | 5 |
| Medium Risk | 5 |
| Standard / Low Risk | 5 |
| Total | 15 |

---

## 3. Legal Issues Covered

### 3.1 Unlimited Liability

Unlimited liability can expose a party to significant financial
exposure because the agreement does not establish a monetary limit.

Example:

"Vendor shall be liable for all direct, indirect, incidental,
and consequential damages without any monetary cap."

Risk:

High Risk

---

### 3.2 Broad Indemnification

Broad indemnification can transfer significant legal and financial
responsibility from one party to another.

Important indicators include:

- Unilateral indemnification
- Broad third-party claims
- Unlimited indemnification
- Responsibility for another party's negligence

Risk:

High Risk

---

### 3.3 Immediate Termination

Immediate termination rights can create business continuity risk,
especially when there is no cure period.

Important indicators include:

- Immediate termination
- Termination without notice
- Termination for minor breaches
- No opportunity to cure
- Broad discretionary termination

Risk:

High Risk

---

### 3.4 Unilateral Pricing Changes

A party may create commercial risk when it can change service fees
without receiving approval from the other party.

Important indicators include:

- Sole discretion
- Short notice
- Unilateral fee changes
- No customer approval

Risk:

Medium Risk

---

### 3.5 Ambiguous Notice Periods

Terms such as "reasonable period" can create uncertainty because
the contract does not establish a precise deadline.

Risk:

Medium Risk

---

### 3.6 Vendor-Controlled Payment Terms

Payment terms can create commercial uncertainty when one party
controls the payment schedule.

Risk:

Medium Risk

---

### 3.7 Unilateral Scope Changes

Allowing one party to modify service scope and associated charges
without approval may create financial and contractual uncertainty.

Risk:

Medium Risk

---

## 4. Prompt Strategies

### Zero-Shot

The model receives:

- Role/persona
- Instructions
- Category definitions

No classification examples are provided.

### Few-Shot

The model receives:

- Role/persona
- Instructions
- Category definitions
- 2 examples for each risk category
- Brief reasoning for each example

---

## 5. Benchmark Results

The following values must be populated from the actual
`metrics.py` execution.

| Metric | Zero-Shot | Few-Shot |
|---|---:|---:|
| Accuracy | TBD | TBD |
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| Macro F1 | TBD | TBD |
| Average Input Tokens | TBD | TBD |
| Average Output Tokens | TBD | TBD |
| Average Total Tokens | TBD | TBD |
| Average Latency | TBD | TBD |

Do not manually fabricate these values.

---

## 6. Confusion Matrix

### Zero-Shot

```text
TBD
