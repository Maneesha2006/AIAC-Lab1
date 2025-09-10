def process_scores(scores):
    if not scores:
        print("No scores entered.")
        return
    avg = sum(scores) / len(scores)
    print(f"Average: {avg}\nHighest: {max(scores)}\nLowest: {min(scores)}")

try:
    scores = list(map(float, input("Enter scores separated by spaces: ").split()))
    process_scores(scores)
except ValueError:
    print("Please enter valid numbers separated by spaces.")
    
