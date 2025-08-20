def collect_and_review_products():
    """
    Collects product names from the user, displays them transparently,
    and allows the user to provide unbiased feedback for each product.
    Ethical guidelines:
    - No product is favored or promoted over others.
    - User feedback is collected fairly for all products.
    - Comments are provided for transparency.
    """

    # Collect product names from the user
    products_input = input("Enter product names separated by commas: ")
    # Split and strip whitespace
    products = [p.strip() for p in products_input.split(",") if p.strip()]

    if not products:
        print("No products entered. Exiting.")
        return

    print("\nYou entered the following products:")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product}")

    # Feedback options for fairness and transparency
    feedback_options = [
        "Excellent",
        "Good",
        "Average",
        "Poor",
        "No opinion"
    ]

    # Collect feedback for each product
    product_feedback = {}
    for product in products:
        print(f"\nPlease provide your feedback for '{product}':")
        for i, option in enumerate(feedback_options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                choice = int(input("Enter the number corresponding to your feedback: "))
                if 1 <= choice <= len(feedback_options):
                    product_feedback[product] = feedback_options[choice - 1]
                    break
                else:
                    print("Please enter a valid number from the options above.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Display the collected feedback transparently
    print("\nCollected Product Feedback (no favoritism shown):")
    for product, feedback in product_feedback.items():
        print(f"Product: {product} | Feedback: {feedback}")

# Run the function
collect_and_review_products()
