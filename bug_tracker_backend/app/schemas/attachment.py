from pydantic import BaseModel

class AttachmentOut(BaseModel):
    id: int
    filename: str
    ticket_id: int

    class Config:
        from_attributes = True
