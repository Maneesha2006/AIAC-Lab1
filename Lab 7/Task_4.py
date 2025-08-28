def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[j] - values[i] != 0:
                ratio = values[i] / (values[j] - values[i])
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  # Avoid division by zero
    return results

num = [5, 10, 15, 20, 25]
print(compute_ratios(num))
