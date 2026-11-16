from flask import Flask, request, jsonify

app = Flask(__name__)
books = []


def next_id():
    return max((book["id"] for book in books), default=0) + 1


@app.get("/books")
def list_books():
    """Return all library books."""
    return jsonify(books), 200


@app.post("/books")
def add_book():
    """Add a book using JSON fields: title, author, and availability."""
    data = request.get_json(silent=True) or {}

    if not data.get("title"):
        return jsonify({"error": "Book title is required"}), 400

    book = {
        "id": next_id(),
        "title": data["title"],
        "author": data.get("author"),
        "available": data.get("available", True),
    }
    books.append(book)
    return jsonify(book), 201


@app.get("/books/<int:book_id>")
def get_book(book_id):
    """Return details for one book."""
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200


@app.patch("/books/<int:book_id>")
def update_book(book_id):
    """Update selected book fields, such as availability."""
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Provide at least one field to update"}), 400

    for field in ("title", "author", "available"):
        if field in data:
            book[field] = data[field]

    return jsonify(book), 200


@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    """Delete a book by ID."""
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": "Book deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)