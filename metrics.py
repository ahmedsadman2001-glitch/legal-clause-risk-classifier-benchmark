import json

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


LABELS = [
    "High Risk",
    "Medium Risk",
    "Standard / Low Risk"
]


def load_results():

    with open(
        "benchmark_results.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def calculate_quality_metrics(results, strategy):

    rows = [
        row
        for row in results
        if row["strategy"] == strategy
        and row["prediction"] != "ERROR"
    ]

    y_true = [
        row["ground_truth"]
        for row in rows
    ]

    y_pred = [
        row["prediction"]
        for row in rows
    ]

    return {

        "sample_count": len(rows),

        "accuracy": round(
            accuracy_score(y_true, y_pred),
            4
        ),

        "macro_precision": round(
            precision_score(
                y_true,
                y_pred,
                labels=LABELS,
                average="macro",
                zero_division=0
            ),
            4
        ),

        "macro_recall": round(
            recall_score(
                y_true,
                y_pred,
                labels=LABELS,
                average="macro",
                zero_division=0
            ),
            4
        ),

        "macro_f1": round(
            f1_score(
                y_true,
                y_pred,
                labels=LABELS,
                average="macro",
                zero_division=0
            ),
            4
        ),

        "confusion_matrix": confusion_matrix(
            y_true,
            y_pred,
            labels=LABELS
        ).tolist(),

        "classification_report": classification_report(
            y_true,
            y_pred,
            labels=LABELS,
            zero_division=0
        )
    }


def calculate_efficiency_metrics(results, strategy):

    rows = [
        row
        for row in results
        if row["strategy"] == strategy
        and row["prediction"] != "ERROR"
    ]

    df = pd.DataFrame(rows)

    return {

        "avg_input_tokens": round(
            df["input_tokens"].mean(),
            2
        ),

        "avg_output_tokens": round(
            df["output_tokens"].mean(),
            2
        ),

        "avg_total_tokens": round(
            df["total_tokens"].mean(),
            2
        ),

        "avg_latency_ms": round(
            df["latency_ms"].mean(),
            2
        ),

        "total_input_tokens": int(
            df["input_tokens"].sum()
        ),

        "total_output_tokens": int(
            df["output_tokens"].sum()
        ),

        "total_tokens": int(
            df["total_tokens"].sum()
        )
    }


def main():

    results = load_results()

    final_metrics = {}

    for strategy in [
        "zero_shot",
        "few_shot"
    ]:

        quality = calculate_quality_metrics(
            results,
            strategy
        )

        efficiency = calculate_efficiency_metrics(
            results,
            strategy
        )

        final_metrics[strategy] = {
            "quality": quality,
            "efficiency": efficiency
        }

        print("\n" + "=" * 60)
        print(strategy.upper())
        print("=" * 60)

        print(
            "Accuracy:",
            quality["accuracy"]
        )

        print(
            "Macro Precision:",
            quality["macro_precision"]
        )

        print(
            "Macro Recall:",
            quality["macro_recall"]
        )

        print(
            "Macro F1:",
            quality["macro_f1"]
        )

        print(
            "Average Input Tokens:",
            efficiency["avg_input_tokens"]
        )

        print(
            "Average Output Tokens:",
            efficiency["avg_output_tokens"]
        )

        print(
            "Average Total Tokens:",
            efficiency["avg_total_tokens"]
        )

        print(
            "Average Latency:",
            efficiency["avg_latency_ms"],
            "ms"
        )

        print("\nConfusion Matrix:")

        matrix = pd.DataFrame(
            quality["confusion_matrix"],
            index=LABELS,
            columns=LABELS
        )

        print(matrix)

        print("\nClassification Report:")
        print(quality["classification_report"])

    with open(
        "metrics_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            final_metrics,
            file,
            indent=2
        )

    print("\nSaved: metrics_results.json")


if __name__ == "__main__":
    main()
