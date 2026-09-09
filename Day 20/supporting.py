from dataclasses import dataclass
from enum import StrEnum
from datetime import datetime, timedelta

#statuses of books
class Status(StrEnum):
    LOANED = "loaned"
    AVAILABLE = "available"

@dataclass
class Book:
    title: str
    author: str
    bookID: int
    status: Status = Status.AVAILABLE

@dataclass
class Member:
    name: str
    memberID: int

@dataclass
class Loan:
    checkoutDate = datetime.now()
    dueDate: datetime = checkoutDate + timedelta(weeks=3)
    book: int
    member: int

class Library:
    activeLoans = dict()
    books = dict()
    members = dict()

    memberID = 001
    bookID = 001

    @classmethod
    def showBooks(cls):
        for book in Library.books:
            print('{} | {} | {} | {}'.format(
                book.title, book.author, book.bookID, book.status.value))

    @classmethod
    def registerMember(cls, name):
        newMember = Member(name, Library.memberID)
        Library.members[Library.memberID] = newMember
        memberID += 1

    @classmethod
    def addBook(cls, title, author):
        newBook = Book(title, author, Library.bookID)
        Library.books[Library.bookID] = newBook
        Library.bookID += 1

    @classmethod
    def checkoutBook(cls, bookN, memberN):
        pass

    @classmethod
    def returnBook(cls, bookN, memberN):
        pass

    @classmethod
    def _findBookID(cls, bookN):
        for i in Library.books:
            for k, book in i:
                if book.name == bookN:
                    return k

    @classmethod
    def _findmemberID(cls, memberN):
        for i in Library.members:
            for k, member in i:
                if member.name == memberN:
                    return k