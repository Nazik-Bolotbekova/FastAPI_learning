from fastapi import FastAPI
from auth_routes import router as auth_router
from order_routes import router as orders_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(orders_router)