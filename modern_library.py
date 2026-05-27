import json
import os

DATA_FILE = "books.json"


def load_books():
    books = []

    if not os.path.exists(DATA_FILE):
        return books

    try:
        f = open(DATA_FILE, "r", encoding="utf-8")
        books = json.load(f)
        f.close()
    except json.JSONDecodeError:
        print("JSON Format Error")
        return []
    except OSError:
        return []

    if not isinstance(books, list):
        print("JSON Format Error")
        return []

    valid_books = []
    for book in books:
        if not isinstance(book, dict):
            continue

        if "title" not in book or "isbn" not in book or "status" not in book:
            continue

        valid_books.append({
            "title": book["title"],
            "isbn": book["isbn"],
            "status": book["status"],
        })

    return valid_books



def save_books(books):
    f = open(DATA_FILE, "w", encoding="utf-8")
    json.dump(books, f, ensure_ascii=False, indent=2)
    f.close()


def isbn_exists(books, isbn):
    for book in books:
        if book["isbn"] == isbn:
            return True
    return False


def show_books(books):
    for book in books:
        print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")


def add_book(books, command_text):
    book_data = command_text.split("/")

    if len(book_data) != 3:
        print("Format Error")
        return

    title = book_data[0].strip()
    isbn = book_data[1].strip()
    status = book_data[2].strip()

    if title == "" or isbn == "" or status == "":
        print("Format Error")
        return

    if status not in ["available", "borrowed"]:
        print("Format Error")
        return

    if isbn_exists(books, isbn):
        print("ISBN Exist")
        return

    books.append({"title": title, "isbn": isbn, "status": status})
    print("Success")


def borrow_book(books, isbn):
    for book in books:
        if book["isbn"] == isbn:
            book["status"] = "borrowed"
            print("Updated")
            return

    print("Book Not Found")


def main():
    books = load_books()
    print("=== 圖書管理系統 v0.1 (Modern) ===")

    while True:
        command = input("> ").strip()

        if command == "exit":
            save_books(books)
            print("系統關閉")
            break

        elif command.startswith("add "):
            add_book(books, command[4:])

        elif command == "show":
            show_books(books)

        elif command.startswith("borrow "):
            borrow_book(books, command[7:])

        else:
            print("Unknown Command")


if __name__ == "__main__":
    main()