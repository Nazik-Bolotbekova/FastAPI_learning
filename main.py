from fastapi import FastAPI

from auth_routes import router as auth_router

app = FastAPI()

@app.get('/endpoint')
async def say_hi():
    return "Hello world, I am learning FastAPI"

@app.get('/some_text')
async def text():
    return {"text" : 'lock in'}

app.include_router(auth_router)