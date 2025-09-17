import csv
import time
from bisect import bisect_left

# Load CSV data
def load_library_data(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Linear Search
def linear_search(data, keyword):
    keyword = keyword.lower()
    return [entry for entry in data if keyword in entry['title'].lower() or keyword in entry['author'].lower()]

# Binary Search (on sorted titles)
def binary_search(data, keyword):
    titles = [entry['title'].lower() for entry in data]
    keyword = keyword.lower()
    index = bisect_left(titles, keyword)
    results = []
    # Collect all matches starting from index
    while index < len(data) and keyword in titles[index]:
        results.append(data[index])
        index += 1
    return results

# Hash-based Search (exact match only)
def build_hash_map(data):
    return {
        entry['title'].lower(): entry
        for entry in data
    }

def hash_search(hash_map, keyword):
    return [hash_map[keyword.lower()]] if keyword.lower() in hash_map else []

# Performance Comparison
def compare_search_methods(data, keyword):
    sorted_data = sorted(data, key=lambda x: x['title'].lower())
    hash_map = build_hash_map(data)

    print(f"\n🔍 Searching for: '{keyword}'")

    # Linear Search
    start = time.time()
    linear_results = linear_search(data, keyword)
    linear_time = time.time() - start

    # Binary Search
    start = time.time()
    binary_results = binary_search(sorted_data, keyword)
    binary_time = time.time() - start

    # Hash Search
    start = time.time()
    hash_results = hash_search(hash_map, keyword)
    hash_time = time.time() - start

    print(f"Linear Search: {len(linear_results)} results in {linear_time:.6f}s")
    print(f"Binary Search: {len(binary_results)} results in {binary_time:.6f}s")
    print(f"Hash Search:   {len(hash_results)} results in {hash_time:.6f}s")

# Example usage
if __name__ == "__main__":
    # Replace with your actual CSV file path
    filename = "library_data.csv"
    data = load_library_data(filename)

    # Test keyword
    test_keyword = "machine learning"
    compare_search_methods(data, test_keyword)
