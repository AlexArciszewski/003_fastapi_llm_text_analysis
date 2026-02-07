
from typing import List, Dict
from transformers import pipeline

#Hugging Face automatically selects the model for the sentiment-analysis pipeline.
analyzer = pipeline("sentiment-analysis")

print("Using model:", analyzer.tokenizer.name_or_path)


def analyze_text(text: str) -> str:
    """
    Analyzes the given text using an LLM model.

    Args:
        text (str): The text to be analyzed.

    Returns:
        str: The analysis result as a string.
    """

    results: List[Dict[str, str]] = analyzer(text)

    return str(results)