RISK_CATEGORIES = """
High Risk:
Clauses creating significant legal or financial exposure, including
uncapped liability, unilateral indemnity obligations, or immediate
or unrestricted termination rights.

Medium Risk:
Clauses containing ambiguous, discretionary, or potentially unfavorable
commercial terms, such as ambiguous notice periods, arbitrary payment
conditions, or unilateral commercial changes.

Standard / Low Risk:
Ordinary, balanced, mutual, and clearly defined commercial terms that
do not create unusual legal or financial exposure.
"""

OUTPUT_INSTRUCTION = """
Return exactly one JSON object:

{
  "risk_category": "High Risk | Medium Risk | Standard / Low Risk",
  "reasoning": "Brief explanation."
}

Do not add markdown or additional fields.
"""

ZERO_SHOT_PROMPT = f"""
You are a LegalTech contract-risk classification assistant.

Classify the following contract clause into exactly one risk category.

{RISK_CATEGORIES}

Rules:
1. Evaluate the actual contractual obligation and allocation of risk.
2. Determine whether rights and obligations are mutual or unilateral.
3. Pay attention to unlimited liability, broad indemnification,
   immediate termination, unilateral pricing changes, ambiguity,
   and balanced commercial terms.
4. Do not invent facts.
5. Select exactly one category.

{OUTPUT_INSTRUCTION}

Contract clause:
{{clause}}
"""

FEW_SHOT_PROMPT = f"""
You are a LegalTech contract-risk classification assistant.

Classify the following contract clause into exactly one risk category.

{RISK_CATEGORIES}

Examples:

EXAMPLE 1
Clause:
"Vendor shall be liable for all direct, indirect, incidental,
and consequential damages without any monetary cap."

Reasoning:
The clause creates unlimited financial exposure.

Classification:
High Risk

EXAMPLE 2
Clause:
"Client shall indemnify, defend, and hold harmless Vendor from
third-party claims arising from deliverables created entirely by Vendor."

Reasoning:
The indemnification obligation is unilateral and creates potentially
significant exposure for the Client.

Classification:
High Risk

EXAMPLE 3
Clause:
"The Company may modify service fees at its sole discretion upon
five business days' notice by email."

Reasoning:
The Company has unilateral pricing discretion and provides a short
notice period.

Classification:
Medium Risk

EXAMPLE 4
Clause:
"Customer shall provide notice of any service issue within a
reasonable period following discovery."

Reasoning:
The phrase "reasonable period" creates an ambiguous deadline.

Classification:
Medium Risk

EXAMPLE 5
Clause:
"Either party may terminate this Agreement by providing at least
30 days' prior written notice."

Reasoning:
The termination right is mutual and the notice period is clearly defined.

Classification:
Standard / Low Risk

EXAMPLE 6
Clause:
"All invoices are payable within 45 days of receipt. Late payments
will incur interest at a rate of 1.5% per month."

Reasoning:
The payment deadline and late-payment consequence are clearly defined.

Classification:
Standard / Low Risk

Apply the same reasoning to the new clause.

{OUTPUT_INSTRUCTION}

Contract clause:
{{clause}}
"""
