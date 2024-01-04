from models import Book, book_schema , books_schema
from flask import abort, make_response, request
from config import db

def obtain_all():
      authors = Book.query.all()
      return books_schema.dump(authors)

def find_by_id(id):
       
       book = Book.query.get(id)
       
       if book is not None:
             return book_schema.dump(book)
       else:
             abort(404, f"Book with id {id} not found")

def add_book():
    
      book_body = request.get_json()
      new_book = book_schema.load(book_body, session=db.session)
      db.session.add(new_book)
      db.session.commit()

      return book_schema.dump(new_book), 201

def update_book(id):
      existing_book = Book.query.get(id)
      book_body = request.get_json()

      if existing_book:
            update_book = book_schema.load(book_body, session=db.session)
            existing_book.title = update_book.title
            existing_book.read = update_book.read
            db.session.merge(existing_book)
            db.session.commit()
            return book_schema.dump(existing_book), 201
      else:
            abort(404, f"Book with ID {id} not found")
            
def delete(id):
      book = Book.query.get(id)

      if book is not None:
            db.session.delete(book)
            db.session.commit()
            return make_response(f"Book with name {book.title} and ID {book.id} successfully deleted", 200)
      else:
            abort(404, f"Author with id {id} not found")