import json
import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from prompts import ZERO_SHOT_PROMPT, FEW_SHOT_PROMPT


load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL")

if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing.")

if not MODEL:
    raise RuntimeError("OPENAI_MODEL is missing.")

client = OpenAI(api_key=API_KEY)


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "risk_category": {
            "type": "string",
            "enum": [
                "High Risk",
                "Medium Risk",
                "Standard / Low Risk"
            ]
        },
        "reasoning": {
            "type": "string"
        }
    },
    "required": [
        "risk_category",
        "reasoning"
    ],
    "additionalProperties": False
}


def classify_clause(clause, prompt_template):

    prompt = prompt_template.format(clause=clause)

    start_time = time.perf_counter()

    response = client.responses.create(
        model=MODEL,
        input=prompt,
        text={
            "format": {
                "type": "json_schema",
                "name": "contract_risk_classification",
                "schema": OUTPUT_SCHEMA,
                "strict": True
            }
        }
    )

    end_time = time.perf_counter()

    latency_ms = (end_time - start_time) * 1000

    result = json.loads(response.output_text)

    usage = response.usage

    return {
        "prediction": result["risk_category"],
        "reasoning": result["reasoning"],
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "total_tokens": usage.total_tokens,
        "latency_ms": round(latency_ms, 2)
    }


def load_dataset():

    with open(
        "test_clauses.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def run_benchmark(dataset):

    results = []

    strategies = {
        "zero_shot": ZERO_SHOT_PROMPT,
        "few_shot": FEW_SHOT_PROMPT
    }

    for strategy, prompt in strategies.items():

        print(f"\nRunning {strategy.upper()}...")

        for item in dataset:

            print(f"Processing Clause {item['id']}")

            try:

                result = classify_clause(
                    item["clause"],
                    prompt
                )

                results.append({
                    "id": item["id"],
                    "clause": item["clause"],
                    "ground_truth": item["ground_truth"],
                    "strategy": strategy,
                    **result
                })

            except Exception as error:

                print(
                    f"Error processing clause {item['id']}: {error}"
                )

                results.append({
                    "id": item["id"],
                    "clause": item["clause"],
                    "ground_truth": item["ground_truth"],
                    "strategy": strategy,
                    "prediction": "ERROR",
                    "reasoning": str(error),
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "latency_ms": 0
                })

    return results


def save_results(results):

    with open(
        "benchmark_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False
        )


if __name__ == "__main__":

    dataset = load_dataset()

    results = run_benchmark(dataset)

    save_results(results)

    print("\nBenchmark completed successfully.")
    print("Results saved to benchmark_results.json")
