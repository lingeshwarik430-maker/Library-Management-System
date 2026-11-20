"""A small, interactive library catalog and book-issue demo."""

BOOKS = [
    {
        "id": "B001",
        "name": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "price": 499.00,
        "issued_to": None,
    },
    {
        "id": "B002",
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 350.00,
        "issued_to": None,
    },
    {
        "id": "B003",
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "price": 299.00,
        "issued_to": None,
    },
]


def display_books(books):
    """Print each book's details and current availability."""
    print("\nLibrary books")
    print("-" * 76)
    print(f"{'ID':<8} {'Book Name':<28} {'Author':<24} {'Price (INR)':>12}  Status")
    print("-" * 76)

    for book in books:
        status = f"Issued to {book['issued_to']}" if book["issued_to"] else "Available"
        print(
            f"{book['id']:<8} {book['name']:<28} {book['author']:<24} "
            f"{book['price']:>12.2f}  {status}"
        )
    print()


def issue_book(books):
    """Issue an available book to the name supplied by the user."""
    book_id = input("Enter the book ID to issue: ").strip().upper()
    book = next((item for item in books if item["id"] == book_id), None)

    if book is None:
        print(f"No book found with ID {book_id or '(blank)'}.")
        return

    if book["issued_to"] is not None:
        print(f"{book['name']} is already issued to {book['issued_to']}.")
        return

    borrower = input("Enter the borrower's name: ").strip()
    if not borrower:
        print("The borrower's name cannot be blank. The book was not issued.")
        return

    book["issued_to"] = borrower
    print(f"Issued '{book['name']}' to {borrower}.")


def main():
    """Run the interactive library menu."""
    while True:
        print("Library Management System")
        print("1. Display books")
        print("2. Issue a book")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            display_books(BOOKS)
        elif choice == "2":
            issue_book(BOOKS)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
