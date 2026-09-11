from dataclasses import dataclass
from enum import StrEnum
from datetime import datetime, timedelta

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
    book: int
    member: int
    checkoutDate: datetime = datetime.now()
    dueDate: datetime = checkoutDate + timedelta(weeks=3)

class Library:
    activeLoans = dict()
    books = dict()
    members = dict()

    memberID = 1
    bookID = 1

    @classmethod
    def showBooks(cls):
        for book in Library.books:
            print('{} | {} | {} | {}'.format(
                book.title, book.author, book.bookID, book.status.value))

    @classmethod
    def registerMember(cls, name):
        newMember = Member(name, Library.memberID)
        Library.members[Library.memberID] = newMember
        Library.memberID += 1

    @classmethod
    def addBook(cls, title, author):
        newBook = Book(title, author, Library.bookID)
        Library.books[Library.bookID] = newBook
        Library.bookID += 1

    @classmethod
    def checkoutBook(cls, bookN, memberN):
        bID = Library._findBookID(bookN)
        mID = Library._findmemberID(memberN)
        if Library.books[bID].status.name == "AVAILABLE" and Library.members[mID]:
            Library.books[bID].status = 'loaned'
            newLoan = Loan(bID, mID)
            Library.activeLoans[bID] = newLoan
        elif Library.books[bID].status.name == 'LOANED':
            raise "Book not currently available"
        else:
            raise "Member not registered at this library"

    @classmethod
    def returnBook(cls, bookN):
        bID = Library._findBookID(bookN)
        loanToDelete = 0
        for i in Library.activeLoans.items():
            if i[0] == bID:
                loanToDelete = bID
        if loanToDelete != 0:
            print("Book successfully returned.")
            Library.books[bID].status = 'available'
        else:
            print("Unable to return book")


    @classmethod
    def _findBookID(cls, bookN):
        for i in Library.books.items():
            if i[1].title == bookN:
                return i[0]

    @classmethod
    def _findmemberID(cls, memberN):
        for i in Library.members.items():
            if i[1].name == memberN:
                return i[0]