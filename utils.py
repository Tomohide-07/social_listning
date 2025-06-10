import re

def clean_text(text: str) -> str:
    """
    Remove URLs and user mentions for anonymization.
    """
    return re.sub(r"(http\S+)|(@\w+)", "", text).strip()