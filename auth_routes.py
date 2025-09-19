from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/authenticate')
async def register():
    return {"message": "Welcome! What is your name?"}
