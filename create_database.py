from config import app, db
from models import Book, Author

AUTHORS_BOOKS = [
    {
        "name": "Jack Kerouac",    
        "books": [
            ('On the Road', 1),
        ],
    },
    {
        "name": "J. K. Rowling",    
        "books": [
            ('Harry Potter and the Philosopher\'s Stone', 0),
        ],
    },
    {
        "name": "Dr. Seuss",    
        "books": [
            ('Green Eggs and Ham', 1),
        ],
    },
]

with app.app.app_context():
    db.drop_all()
    db.create_all()
    for author in AUTHORS_BOOKS:
        new_author = Author(name=author.get("name"))
        for book_title, read in author.get("books", []):
            new_author.books.append(
                Book(
                    title=book_title,
                    read=read,
                )
            )
        db.session.add(new_author)
    db.session.commit()