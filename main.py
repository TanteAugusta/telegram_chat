from fastapi import FastAPI

from services.telegram import get_chat_messages

app = FastAPI()


@app.get("/")
async def read_root():
    return {"status": "working"}


@app.get("/get_items")
async def read_item():
    lst_of_messages = await get_chat_messages()
    return {"messages": lst_of_messages}
