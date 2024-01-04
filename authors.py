from models import Author, author_schema, authors_schema, books_schema
from flask import abort, make_response, request
from config import db

            
def obtain_all():
      authors = Author.query.all()
      return authors_schema.dump(authors)

def add_author():
      author_body = request.get_json()
      new_author = author_schema.load(author_body, session=db.session)
      db.session.add(new_author)
      db.session.commit()

      return author_schema.dump(new_author), 201
        

def find_by_id(id):
       
       author = Author.query.get(id)
       
       if author is not None:
             return author_schema.dump(author)
       else:
             abort(404, f"Author with id {id} not found")

def update_author(id):
      existing_author = Author.query.get(id)
      update_author_body = request.get_json()

      if existing_author:
            author_schema.load(existing_author, session=db.session)
            existing_author.name = update_author_body.name
            db.session.merge(existing_author)
            db.session.commit()
            return author_schema.dump(existing_author), 201
      else:
            abort(404, f"Author with ID {id} not found")

def delete(id):
      author = Author.query.get(id)

      if author is not None:
            db.session.delete(author)
            db.session.commit()
            return make_response(f"Author with name {author.name} and ID {author.id} successfully deleted", 200)
      else:
            abort(404, f"Author with id {id} not found")
