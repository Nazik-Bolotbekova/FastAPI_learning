from fastapi import APIRouter

router = APIRouter(prefix='/orders',tags=['orders'])

@router.get('/orders')
async def get_orders():
    return {'message': 'Welcome to the Orders API!'}
