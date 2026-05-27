import os

DATA_FILE = "lib_data.txt"


def load_books():
    books = []

    if not os.path.exists(DATA_FILE):
        return books

    f = open(DATA_FILE, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    for line in lines:
        parts = line.strip().split("@@")
        if len(parts) != 2:
            continue

        book_data = parts[1].split("##")
        if len(book_data) != 2:
            continue

        books.append({
            "title": parts[0],
            "isbn": book_data[0],
            "status": book_data[1],
        })

    return books


def save_books(books):
    f = open(DATA_FILE, "w", encoding="utf-8")

    for book in books:
        f.write(f"{book['title']}@@{book['isbn']}##{book['status']}\n")

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

    title = book_data[0]
    isbn = book_data[1]
    status = book_data[2]

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