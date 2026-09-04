from dataclasses import dataclass
from enum import strEnum

class TicketStatus(strEnum):
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