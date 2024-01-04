from config import db, ma
from marshmallow_sqlalchemy import fields
import uuid

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    title = db.Column(db.String(100))
    author_ID = db.Column(db.String(32), db.ForeignKey('author.id'))
    read = db.Column(db.Boolean)

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(32))
    
    books = db.relationship(
        Book,
        backref="author_id",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Book.id)"
    )


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session
        include_relationships = True


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    
    books = fields.Nested(BookSchema, many=True)


book_schema = BookSchema()
books_schema = BookSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)