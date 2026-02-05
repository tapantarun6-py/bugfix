from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, admin_only
from app.models.project import Project

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/")
def create_project(
    name: str,
    description: str,
    db: Session = Depends(get_db),
    admin = Depends(admin_only)
):
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("/")
def list_projects(
    db: Session = Depends(get_db),
    admin = Depends(admin_only)
):
    return db.query(Project).all()
