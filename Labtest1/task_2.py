def choose_book():
    books = {
        "comedy": ["The Hitchhiker's Guide to the Galaxy", "Good Omens", "Bossypants"],
        "horror": ["The Shining", "The Last Day", "It", "Bird Box"],
        "romantic": ["Titanic", "Pride and Prejudice", "The Notebook"],
        "science fiction": ["Dune", "Ender's Game", "Neuromancer"],
        "fantasy": ["Harry Potter and the Sorcerer's Stone", "The Hobbit", "Mistborn"],
        "mystery": ["Gone Girl", "The Girl with the Dragon Tattoo", "Sherlock Holmes"],
        "historical": ["The Book Thief", "All the Light We Cannot See", "Wolf Hall"],
        "thriller": ["The Da Vinci Code", "The Girl on the Train", "Before I Go to Sleep"]
    }

    print("Available genres:")
    for genre in books:
        print(f"- {genre}")

    user_genre = input("Enter the genre you are interested in: ").strip().lower()
    if user_genre not in books:
        print("Sorry, that genre is not available.")
        return

    print(f"Available books in {user_genre.title()}:")
    for idx, book in enumerate(books[user_genre], 1):
        print(f"{idx}. {book}")

    user_choice = input("Enter the name of the book you want to read: ").strip()
    if user_choice in books[user_genre]:
        print(f"Great choice! Enjoy reading '{user_choice}'.")
    else:
        print("Sorry, that book is not available in the selected genre.")

if __name__ == "__main__":
    choose_book()
