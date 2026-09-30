test_cases = [
    {
        "question": "What is machine learning?",
        "expected_topic": "machine learning",
    },
    {
        "question": "What is deep learning?",
        "expected_topic": "deep learning",
    },
    {
        "question": "What is the main topic of the document?",
        "expected_topic": "document",
    },
]


for case in test_cases:

    print("=" * 50)

    print("Question:")
    print(case["question"])

    print("Expected topic:")
    print(case["expected_topic"])