from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    ticket_id: int

class CommentOut(BaseModel):
    id: int
    content: str
    ticket_id: int

    class Config:
        orm_mode = True
