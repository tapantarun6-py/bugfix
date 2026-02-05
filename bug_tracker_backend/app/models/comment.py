from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
