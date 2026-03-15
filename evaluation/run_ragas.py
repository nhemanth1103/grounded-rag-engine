from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

data = {
    "question": ["What is transformer architecture?"],
    "answer": ["generated answer"],
    "contexts": [["retrieved chunk text"]],
}

dataset = Dataset.from_dict(data)

result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy]
)

print(result)