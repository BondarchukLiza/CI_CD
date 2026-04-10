def write_result(filepath: str, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        for word, count in data:
            f.write(f"{word}-{count}\n")