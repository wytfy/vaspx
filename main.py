from typing import Optional
import uvicorn
from fastapi import FastAPI
from routers import system_api

app = FastAPI()

app.include_router(system_api.router, prefix='/system')


@app.get("/")
def read_root():
    return "Hello World!"


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=80, reload=True, debug=True)
