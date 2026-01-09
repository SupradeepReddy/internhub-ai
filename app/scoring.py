def calculate_score(matched, total):
    if total == 0:
        return 50
    return round((matched / total) * 100, 2)
