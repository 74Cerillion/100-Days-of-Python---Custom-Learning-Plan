import sys
import json
import datetime
from pathlib import Path
from supporting import Library, Book, Member, Loan

def main():

    curPath = Path(__file__).resolve().parent
    save = curPath / 'currentState.json'

    try:
        with open(save, 'r') as f:
            currentState = json.load(f)

            for book in currentState["books"]:
                for k, v in book:
                    foundBook = Book(v["title"], v["author"], int(v["bookID"]), 
                                                                v["status"])
                    Library.books[int(foundBook.bookID)] = foundBook

            for member in currentState["members"]:
                for k, v in member:
                    foundMember = Member(v["name"], int(v["memberID"]))
                    Library.members[int(foundMember.memberID)] = foundMember

            for loan in currentState["loans"]:
                for k, v in loan:
                    foundLoan = Loan(
                                int(v['book']),
                                int(v['member']), 
                                datetime(v['checkoutDate']), 
                                datetime(v['dueDate']))
                    Library.activeLoans[int(k)] = foundLoan

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
        choice = choice.lower()
        choice = choice[0, 3]

        if userChoice == 'add':
            pass

        elif userChoice == 'reg':
            pass

        elif userChoice == 'che':
            pass

        elif userChoice == 'ret':
            pass

        else:
            with open(save, 'rw') as f:
                json.dump(Library.activeLoans, f)
                json.dump(Library.books, f)
                json.dump(Library.members, f)
                json.dump(Library.bookID, f)
                json.dump(Library.memberID, f)
            sys.exit(1)