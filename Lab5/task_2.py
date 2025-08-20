def analyze_sentiment():
    text = input("Enter some text: ")

    # Simple lists of positive and negative words
    positive_words = ['good', 'great', 'happy', 'excellent', 'awesome', 'fantastic', 'love', 'nice', 'wonderful', 'amazing', 'positive']
    negative_words = ['bad', 'sad', 'terrible', 'awful', 'hate', 'horrible', 'poor', 'worst', 'negative', 'angry']

    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Count positive and negative words
    pos_count = sum(word in positive_words for word in words)
    neg_count = sum(word in negative_words for word in words)

    # Determine sentiment
    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentiment of the text: {sentiment}")

# Run the function
analyze_sentiment()
