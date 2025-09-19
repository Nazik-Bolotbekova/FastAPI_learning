from fastapi import FastAPI

app = FastAPI()

@app.get('/endpoint')
async def say_hi():
    return "Hello world, I am learning FastAPI"

@app.get('/some_text')
async def text():
    return {"text" : 'lock in'}