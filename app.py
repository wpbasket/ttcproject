from fastapi import FastAPI,Request
from uvicorn import run
app=FastAPI
async def home():
    return "Hello, wp"
if __name__=="__main__":
    run("app:app",host="0.0.0.0",port=8000,reload=True)