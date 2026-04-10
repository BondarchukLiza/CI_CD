import re
from collections import Counter


def get_top_words(text: str, top_n: int = 10):
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(top_n)