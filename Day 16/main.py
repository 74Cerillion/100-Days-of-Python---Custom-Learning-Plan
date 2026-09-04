from dataclasses import dataclass
from enum import StrEnum

class TicketStatus(StrEnum):
    pending = 'Pending'
    in_progress = 'In Progress'
    resolved = 'Resolved'
    closed = 'Closed'

@dataclass
class Ticket:
    id: int
    title: str
    status: TicketStatus = TicketStatus.pending

    def __post_init__(self):
        if not isinstance(self.status, TicketStatus):
            raise ValueError(
                f"Invalid status: {self.status}. Must be a TicketStatus."
                )

    def advance(self):
        if self.status == TicketStatus.pending:
            self.status = TicketStatus.in_progress
        elif self.status == TicketStatus.in_progress:
            self.status = TicketStatus.resolved
        elif self.status == TicketStatus.resolved:
            self.status = TicketStatus.closed
        else:
            raise ValueError("Cannot advance a closed ticket.")

def main():
    ticket1 = Ticket(id=1, title="Fix login bug")
    print(ticket1)

    ticket1.advance()
    print(ticket1)

    ticket1.advance()
    print(ticket1)

    ticket1.advance()
    print(ticket1)

    print(ticket1.status.name)  # Output: closed
    print(ticket1.status.value)  # Output: Closed

    try:
        ticket1.advance()
    except ValueError as e:
        print(e)

    ticket2 = Ticket(id=2, title="Add new feature", status=TicketStatus.in_progress)
    print(ticket2)

    ticket3 = Ticket(id=3, title="Update documentation", status='active')
      # This will raise a ValueError)

    print(ticket3)

if __name__ == "__main__":
    main()