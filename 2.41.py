import json
from typing import List, Dict, Any


def load_books(filepath: str) -> List[Dict[str, Any]]:
    """
    Load a list of books from a JSON file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        List of book dictionaries.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
        ValueError: If the root JSON element is not a list.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Catalog root must be a list of books.")

    return data


def save_books(filepath: str, books: List[Dict[str, Any]], indent: int = 4) -> None:
    """
    Save a list of books to a JSON file.

    Args:
        filepath: Path where the JSON file will be written.
        books: List of book dictionaries to serialize.
        indent: Indentation level for pretty printing (default 4).

    Raises:
        TypeError: If books is not a list.
    """
    if not isinstance(books, list):
        raise TypeError("books must be a list")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=indent)


def add_book(
    books: List[Dict[str, Any]],
    book_id: int,
    title: str,
    author: str,
    year: int,
    genres: List[str],
    is_available: bool = True
) -> Dict[str, Any]:
    """
    Add a new book to the books list.

    Args:
        books: Existing list of book dictionaries.
        book_id: Unique integer ID of the book.
        title: Title of the book.
        author: Author name.
        year: Year of publication.
        genres: List of genres.
        is_available: Availability status (default True).

    Returns:
        The newly created book dictionary.

    Raises:
        ValueError: If a book with book_id already exists or title is empty.
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty")

    for book in books:
        if book.get("id") == book_id:
            raise ValueError(f"Book with ID {book_id} already exists")

    new_book: Dict[str, Any] = {
        "id": book_id,
        "title": title.strip(),
        "author": author.strip() if isinstance(author, str) else author,
        "year": int(year),
        "genres": list(genres),
        "is_available": bool(is_available),
    }

    books.append(new_book)
    return new_book


def find_books_by_genre(books: List[Dict[str, Any]], genre: str) -> List[Dict[str, Any]]:
    """
    Find all books that belong to a specific genre (case-insensitive).

    Args:
        books: List of book dictionaries.
        genre: The genre name to filter by.

    Returns:
        List of matching book dictionaries.
    """
    target = genre.strip().lower()
    matches = []
    for book in books:
        book_genres = [g.lower() for g in book.get("genres", [])]
        if target in book_genres:
            matches.append(book)
    return matches


def calculate_average_year(books: List[Dict[str, Any]]) -> float:
    """
    Calculate the average publication year of books in the list.

    Args:
        books: List of book dictionaries.

    Returns:
        Average publication year as a float. Returns 0.0 if the list is empty.
    """
    if not books:
        return 0.0

    total_years = sum(book["year"] for book in books)
    return float(total_years / len(books))


      