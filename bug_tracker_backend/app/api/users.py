from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/ping")
def users_ping():
    return {"message": "Users route working"}
