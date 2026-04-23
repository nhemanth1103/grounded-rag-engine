from ragas import evaluate
from ragas.metrics import Faithfulness, AnswerRelevancy
from datasets import Dataset

# Example evaluation dataset
data = {
    "question": [
        "What is transformer architecture?"
    ],
    "answer": [
        "The Transformer architecture uses stacked self-attention layers."
    ],
    "contexts": [
        [
            "The Transformer is a neural network architecture based entirely on attention mechanisms."
        ]
    ]
}

dataset = Dataset.from_dict(data)

# Initialize metrics
metrics = [
    Faithfulness(),
    AnswerRelevancy()
]

result = evaluate(
    dataset=dataset,
    metrics=metrics
)

print("\nRAG Evaluation Results\n")
print(result)