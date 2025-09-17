import random
import heapq
import time

# Step 1: Simulate stock data
def generate_stock_data(n=100):
    symbols = [f"STK{i:03}" for i in range(n)]
    data = []
    for symbol in symbols:
        open_price = round(random.uniform(100, 500), 2)
        close_price = round(open_price * random.uniform(0.95, 1.05), 2)
        change_pct = round(((close_price - open_price) / open_price) * 100, 2)
        data.append({
            "symbol": symbol,
            "open": open_price,
            "close": close_price,
            "change_pct": change_pct
        })
    return data

# Step 2: Heap Sort by percentage change
def heap_sort(data):
    # Include symbol as a tie-breaker to avoid comparing dicts
    heap = [(-stock["change_pct"], stock["symbol"], stock) for stock in data]
    heapq.heapify(heap)
    sorted_data = [heapq.heappop(heap)[2] for _ in range(len(heap))]
    return sorted_data

# Step 3: Build Hash Map for fast lookup
def build_hash_map(data):
    return {stock["symbol"]: stock for stock in data}

# Step 4: Search function using Hash Map
def search_stock(symbol, stock_map):
    return stock_map.get(symbol, "Stock not found")

# Step 5: Performance comparison
def compare_performance(data):
    symbol_to_search = data[len(data)//2]["symbol"]

    # Heap Sort timing
    start = time.time()
    heap_sorted = heap_sort(data)
    heap_sort_time = time.time() - start

    # Built-in sorted() timing
    start = time.time()
    builtin_sorted = sorted(data, key=lambda x: x["change_pct"], reverse=True)
    builtin_sort_time = time.time() - start

    # Hash Map search timing
    stock_map = build_hash_map(data)
    start = time.time()
    result_hash = search_stock(symbol_to_search, stock_map)
    hash_search_time = time.time() - start

    # List search timing
    start = time.time()
    result_list = next((s for s in data if s["symbol"] == symbol_to_search), "Stock not found")
    list_search_time = time.time() - start

    # Print results
    print(f"\n🔍 Performance Comparison:")
    print(f"Heap Sort Time:       {heap_sort_time:.6f} seconds")
    print(f"Built-in Sort Time:   {builtin_sort_time:.6f} seconds")
    print(f"Hash Map Search Time: {hash_search_time:.6f} seconds")
    print(f"List Search Time:     {list_search_time:.6f} seconds")

# Step 6: Run everything
if __name__ == "__main__":
    stock_data = generate_stock_data(1000)  # You can change the number of stocks here
    sorted_stocks = heap_sort(stock_data)
    stock_map = build_hash_map(stock_data)

    # Example search
    print(f"\n📈 Example Search Result for 'STK050':")
    print(search_stock("STK050", stock_map))

    # Compare performance
    compare_performance(stock_data)
