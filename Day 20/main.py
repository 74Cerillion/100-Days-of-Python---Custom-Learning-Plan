import sys
import json
from datetime import datetime
from pathlib import Path
from supporting import Library, Book, Member, Loan, Status

def main():

    curPath = Path(__file__).resolve().parent
    save = curPath / 'currentState.json'

    try:
        with open(save, 'r') as f:
            currentState = json.load(f)

            for book in currentState["books"]:
                for k in book:
                    foundTitle = currentState["books"][k]['title']
                    foundAuthor = currentState["books"][k]['author']
                    foundBookID = int(currentState["books"][k]['bookID'])
                    foundStatus = Status(currentState["books"][k]['status'])
                    foundBook = Book(foundTitle, foundAuthor, foundBookID, 
                                                                foundStatus)
                    Library.books[int(foundBook.bookID)] = foundBook

            for member in currentState["members"]:
                for k in member:
                    foundMember = currentState['members'][k]['name']
                    foundmemberID = int(currentState['members'][k]['memberID'])
                    instantiateMember = Member(foundMember, foundmemberID)
                    Library.members[int(instantiateMember.memberID)] = instantiateMember

            for loan in currentState["activeLoans"]:
                for k in loan:
                    foundBookIDL = int(currentState['activeLoans'][k]['book'])
                    foundMemberIDL = int(currentState['activeLoans'][k]['member'])
                    foundCheckoutDate = currentState['activeLoans'][k]['checkoutDate']
                    foundCheckoutDate = datetime.fromisoformat(foundCheckoutDate)
                    foundDueDate = currentState['activeLoans'][k]['dueDate']
                    foundDueDate = datetime.fromisoformat(foundDueDate)
                    instantiateLoan = Loan(foundBookIDL, foundMemberIDL, foundCheckoutDate, foundDueDate)
                    Library.activeLoans[int(k)] = instantiateLoan

            Library.bookID = currentState["bookID"]
            Library.memberID = currentState["memberID"]
                    
    except FileNotFoundError:
        print('Invalid Filepath')
        sys.exit(1)

    while True:
        print("Welcome to xyz Library!")
        print(r"""
    What are you trying to do?
        ADD. Add a Book to the Library
        REG. Register a new member
        CHE. Check out a book
        RET. Return a currently checked out book
        Q. Save and Quit
    """)
        userChoice = input("Enter your choice: ")
        userChoice = userChoice.lower()

        if userChoice == 'add':
            title = input("What is the book's Title? ")
            author = input("Who is the book's Author? ")
            Library.addBook(title, author)

        elif userChoice == 'reg':
            name = input("What is the new user's name? ")
            Library.registerMember(name)

        elif userChoice == 'che':
            member = input("Member checking out book: ")
            book = input("Title of the book: (case sensitive) ")
            Library.checkoutBook(book, member)

        elif userChoice == 'ret':
            book = input("Enter the Book's Title: ")
            Library.returnBook(book)

        else:

            saveState = dict()

            bookToSave = dict()
            for bookID, b in Library.books.items():
                bDict = {"title": b.title,
                         "author": b.author,
                         "bookID": bookID,
                         "status": str(b.status)
                         }
                bookToSave[bookID] = bDict
            saveState["books"] = bookToSave

            memToSave = dict()
            for memid, mem in Library.members.items():
                memDict = {"name": mem.name,
                           "memberID": memid}
                memToSave[memid] = memDict
            saveState["members"] = memToSave

            loansToSave = dict()
            for bookid, loa in Library.activeLoans.items():
                bloa = {"book": loa.book,
                        "member": loa.member,
                        "checkoutDate": str(loa.checkoutDate),
                        "dueDate": str(loa.dueDate),
                        }
                loansToSave[bookid] = bloa
            saveState["activeLoans"] = loansToSave

            saveState["bookID"] = Library.bookID
            saveState["memberID"] = Library.memberID

            with open(save, 'w') as f:
                json.dump(saveState, f, indent=4)

            sys.exit(1)

if __name__ == '__main__':
    main()