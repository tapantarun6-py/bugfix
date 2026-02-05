from fastapi import FastAPI
from app.core.database import Base, engine

from app.api import auth, users, projects, tickets, comments, ws
from app.api import attachments
app.include_router(attachments.router)


# create tables
Base.metadata.create_all(bind=engine)

# create app FIRST
app = FastAPI(title="Bug Tracker API")

# include routers AFTER app is defined
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tickets.router)
app.include_router(comments.router)
app.include_router(ws.router)
