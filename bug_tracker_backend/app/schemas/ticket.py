from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str
    project_id: int
    assignee_id: int

class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    project_id: int
    assignee_id: int

    class Config:
        orm_mode = True
