from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketOut
from app.models.user import User
from app.core.ws_manager import manager


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.post("/", response_model=TicketOut)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        project_id=ticket.project_id,
        assignee_id=ticket.assignee_id,
        status="TODO"
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.get("/", response_model=list[TicketOut])
def list_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Ticket).all()
@router.patch("/{ticket_id}/status")
async def update_ticket_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if status not in ["TODO", "IN_PROGRESS", "DONE"]:
        return {"error": "Invalid status"}

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        return {"error": "Ticket not found"}

    ticket.status = status
    db.commit()

    await manager.broadcast({
        "type": "TICKET_STATUS_UPDATED",
        "ticket_id": ticket.id,
        "status": status
    })

    return {"message": "Status updated"}

@router.get("/search", response_model=list[TicketOut])
def search_tickets(
    status: str | None = None,
    assignee_id: int | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Ticket)

    if status:
        query = query.filter(Ticket.status == status)
    if assignee_id:
        query = query.filter(Ticket.assignee_id == assignee_id)

    return query.all()
